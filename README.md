
# Deep Research AI System

##  Overview

The **Deep Research AI System** is an agent-based tool designed to conduct comprehensive online research on any given topic. It uses the Tavily API for retrieving web-based information and features a multi-agent architecture that processes and synthesizes findings into well-structured insights.

##  Features

-  **Web Information Gathering**: Uses Tavily's advanced search API for real-time, relevant information retrieval.
-  **Multi-Agent Architecture**:
  - Research Agent for data retrieval.
  - Drafting Agent for transforming raw data into meaningful output.
-  **Information Synthesis**: Automatically extracts and organizes key data from multiple sources.
-  **Detailed Research Output**: Provides comprehensive, source-attributed results.
- 💾 **JSON Export**: Outputs structured research data and findings into a JSON file for further use.

##  System Architecture

The system is designed with a dual-agent architecture:

1. **Research Agent**  
   - Queries the Tavily API  
   - Gathers and filters web data based on the research query

2. **Drafting Agent**  
   - Consumes the output from the Research Agent  
   - Synthesizes the information into a coherent, structured response

3. **Research System Coordinator**  
   - Manages the interaction between agents  
   - Handles input/output and task orchestration

##  How It Works

When prompted, enter your research question. The system will:

1. Research your query using Tavily's search API  
2. Analyze and extract key information from the search results  
3. Synthesize a comprehensive answer based on the gathered information  
4. Display the answer in the console  
5. Save the complete research results to a JSON file  

##  Installation

###  Prerequisites

- Python 3.9 or higher  
- Tavily API Key (Get one from [Tavily](https://tavily.com/))  

###  Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/deep-research-ai.git
   cd deep-research-ai
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your API key**  
   Create a `.env` file in the project root and add:
   ```env
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

4. **Run the system**  
   ```bash
   python main.py
   ```

## 🧾 Code Structure

- `main.py`  
  Main entry point that initializes the research system and handles user interaction.

- `ResearchAgent`  
  Handles web information retrieval:
  - Initializes the Tavily API client  
  - Performs web searches with configurable parameters  
  - Processes and returns structured search results

- `DraftingAgent`  
  Synthesizes information:
  - Extracts key points from search results  
  - Formats and organizes by source  
  - Creates comprehensive research summaries

- `ResearchSystem`  
  Orchestrates the workflow:
  - Initializes and coordinates agents  
  - Manages data flow and export  

##  Example Queries

Here are some examples you can try:

- "What are the main causes of climate change?"
- "How do vaccines work?"
- "What is quantum computing?"
- "What are the latest developments in renewable energy?"
- "What are the differences between artificial intelligence and machine learning?"

##  Limitations

- The quality of research depends on Tavily's search results  
- Limited to information available on the public web  
- Does not have the ability to follow complex reasoning chains  
- No memory of previous research sessions  

##  Future Improvements

- Integration with additional search APIs for broader coverage  
- Implementation of a memory system for context retention  
- Advanced NLP techniques for better information synthesis  
- Supervisor agent to validate and refine research findings  
- Citation formatting for academic research  

##  License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

##  Acknowledgments

- Tavily for providing the search API  
- LangChain community for inspiration on agent-based architectures
