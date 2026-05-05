import os
import requests
from crewai.tools import tool
from duckduckgo_search import DDGS

@tool("Internet_Search")
def internet_search_tool(query: str) -> str:
    """
    Search the internet to verify news claims.
    Returns top 3 search results.
    """
    try:
        results = DDGS().text(query, max_results=3)

        formatted = []
        for r in results:
            formatted.append(
                f"Title: {r.get('title')}\n"
                f"Link: {r.get('link')}\n"
                f"Snippet: {r.get('body')}\n"
                "----------------------"
            )

        return "\n".join(formatted)

    except Exception as e:
        return f"Search Error: {str(e)}"

@tool("Wikipedia_Search")
def wikipedia_search_tool(query: str) -> str:
    """
    Search Wikipedia for background information about a claim, person, or organization.
    """
    try:
        url = "https://en.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json",
            "srlimit": 2
        }
        response = requests.get(url, params=params)
        data = response.json()
        
        results = data.get("query", {}).get("search", [])
        if not results:
            return "No Wikipedia results found."
            
        formatted = []
        for r in results:
            formatted.append(f"Title: {r['title']}\nSnippet: {r['snippet']}\n")
            
        return "\n".join(formatted)
    except Exception as e:
        return f"Wikipedia Error: {str(e)}"


def get_all_tools():
    """
    Return all tools in a list for CrewAI.
    """
    return [internet_search_tool, wikipedia_search_tool]
