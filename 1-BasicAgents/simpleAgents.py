'''
Single Agent
'''

# Importing necessary libraries
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

import os
from dotenv import load_dotenv # For loading the environment variable's values
load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

# Creating the agent
agent = Agent(
  model = Groq(id="llama-3.1-8b-instant"),
  description = "You are a helpful assistant. You task is to reply to teh user question(s)",
  tools = [DuckDuckGoTools()],
  markdown = True
)

# Running the agent (i.e., asking question)
agent.print_response("Who is Alan Walker ?")