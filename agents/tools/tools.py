# Tavily AI is a search API highly optimized for LLM agents, with built-in functionality to take in questions and responds with search queries.
# Generous, 1000 free API credits/month.
from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_url_tavily(name: str):
    """Searches for LinkedIn Profile Page"""
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res[0]["url"]