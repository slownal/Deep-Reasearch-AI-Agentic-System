import os
from dotenv import load_dotenv
from tavily import TavilyClient
from typing import List, Dict
import json

# Load environment variables from .env file
load_dotenv()

class ResearchAgent:
    def __init__(self):
        """Initialize the research agent with Tavily client"""
        tavily_api_key = os.getenv("TAVILY_API_KEY")
        if not tavily_api_key:
            raise ValueError("TAVILY_API_KEY not found in environment variables")
        
        self.client = TavilyClient(api_key=tavily_api_key)
    
    def search(self, query: str, max_results: int = 5) -> List[Dict]:
        """Perform a web search using Tavily API"""
        try:
            search_response = self.client.search(
                query=query,
                search_depth="advanced",
                max_results=max_results,
                include_answer=True,
                include_domains=None,
                exclude_domains=None
            )
            return search_response.get("results", [])
        except Exception as e:
            print(f"Error in Tavily search: {e}")
            return []

class DraftingAgent:
    def __init__(self):
        """Initialize the drafting agent"""
        pass
    
    def extract_key_information(self, search_results: List[Dict]) -> List[str]:
        """Extract important information from search results"""
        key_info = []
        
        for result in search_results:
            # Extract title, content and URL
            title = result.get("title", "")
            content = result.get("content", "")
            url = result.get("url", "")
            
            # Add formatted information to list
            key_info.append(f"Title: {title}\nContent: {content}\nSource: {url}\n")
        
        return key_info
    
    def synthesize_answer(self, query: str, key_info: List[str]) -> str:
        """Synthesize an answer from the key information"""
        answer = f"Research findings for: {query}\n\n"
        
        # Add summary statement
        answer += "Based on the search results, here's a summary of the information:\n\n"
        
        # Add key points from each source
        for i, info in enumerate(key_info, 1):
            answer += f"Source {i}:\n{info}\n"
        
        return answer

class ResearchSystem:
    def __init__(self):
        """Initialize the research system with both agents"""
        self.researcher = ResearchAgent()
        self.drafter = DraftingAgent()
    
    def run(self, query: str) -> Dict:
        """Run the complete research system"""
        # Step 1: Collect search results
        print("Researching your query...")
        search_results = self.researcher.search(query)
        
        # Check if we got results
        if not search_results:
            return {
                "query": query,
                "answer": "I couldn't find any information on this topic. Please try a different query.",
                "search_results": []
            }
        
        # Step 2: Extract key information
        print("Analyzing search results...")
        key_info = self.drafter.extract_key_information(search_results)
        
        # Step 3: Synthesize an answer
        print("Drafting your answer...")
        answer = self.drafter.synthesize_answer(query, key_info)
        
        # Step 4: Return the full result
        return {
            "query": query,
            "answer": answer,
            "search_results": search_results
        }

def save_results(result: Dict, filename: str = "research_results.json"):
    """Save the research results to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
    print(f"Results saved to {filename}")

if __name__ == "__main__":
    # Create and run the research system
    system = ResearchSystem()
    
    # Get the query from the user
    query = input("Enter your research question: ")
    
    # Run the research system
    result = system.run(query)
    
    # Print the answer
    print("\nFinal Answer:")
    print(result["answer"])
    
    # Save the results
    save_results(result)
