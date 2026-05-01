'''
Multiple Agents
'''

# Importing necessary libraries
from agno.agent import Agent
from agno.team import Team
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

import os
from dotenv import load_dotenv # For loading the environment variable's values
load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

# Creating web agent
web_agent = Agent(
  name = "Web Agent",
  role = "Search the web for requested Information",
  model = Groq(id='llama-3.1-8b-instant'),
  tools = [DuckDuckGoTools()],
  instructions = "Always include the sources", # Some explicit instructions you want your agent to follow
  debug_mode = True,
  markdown = True # For markdown support
)

# Creating finance agent
finance_agent = Agent(
  name = "Finance Agent",
  role = "Search the web for financial information about companies.",
  model = OpenAIChat(id='gpt-4o'),
  tools = [YFinanceTools(enable_stock_price = True, enable_analyst_recommendations = True, enable_stock_fundamentals = True, enable_company_info = True)],
  instructions = "Use tables to display data", # Some explicit instructions you want your agent to follow
  debug_mode = True,
  markdown = True # For markdown support
)

# Combining the above 2 agents - as a team
agent_team = Team(
  members = [web_agent, finance_agent],
  model = Groq(id='llama-3.1-8b-instant'),
  instructions = ["Always include sources", "Use tables to display data"],
  debug_mode = True,
  markdown = True,
)

# Get something to ask to the team (the team of agents)
agent_team.print_response("Analyze the stock prices of APple Inc., Tesla, Alphabet, NVIDIA and Microsoft - then suggest which one to buy for long term investment")