# Agentic AI @ `Agno` (`PhiData`) - `V2`
Here, we explore the design and implementation of **Agentic AI systems** ranging from simple single-agent setups to advanced multi-agent orchestration with persistent memory. It leverages frameworks like `agno`, along with LLM providers (`openai`, `groq`), to build agents capable of tool usage, reasoning, and contextual decision-making. The `simpleAgents.py` module demonstrates foundational agent behavior with tool integration (e.g., `duckduckgo-search`, `yfinance`) for real-time data retrieval, while `multiAgents.py` extends this into coordinated multi-agent pipelines where specialized agents collaborate on complex tasks. The `agentMemory.py` module introduces memory-augmented agents using vector stores (`lancedb`, `tantivy`) to persist and retrieve contextual information across interactions, enabling stateful and context-aware reasoning. Additional utilities such as `pypdf` for document parsing and `pandas` for data handling highlight extensibility. The project showcases modular agent design, tool-augmented reasoning, retrieval-backed memory, and scalable multi-agent architectures suitable for building intelligent, adaptive AI systems.
<br>
<br>

## References
[Krish Naik](https://github.com/krishnaik06)<br>
[Agno Framework](https://github.com/agno-ai/agno)<br>
[OpenAI](https://platform.openai.com/)<br>
[Groq](https://github.com/groq/groq-python)<br>
[LanceDB](https://github.com/lancedb/lancedb)<br>
[Tantivy](https://github.com/quickwit-oss/tantivy)
