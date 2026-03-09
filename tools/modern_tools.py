# Standard Library Imports
from datetime import datetime

# Third-Party Library Imports

# Local Application Imports
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper

# Modern
from langchain.tools import tool

search = DuckDuckGoSearchRun()

# Modern
@tool
def search_web(query: str) -> str:
    """Search the web for information"""
    return search.run(query)