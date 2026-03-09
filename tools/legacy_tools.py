# Standard Library Imports
from datetime import datetime

# Third-Party Library Imports

# Local Application Imports
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper

# Legacy
from langchain_classic.tools import Tool

search = DuckDuckGoSearchRun()

# Legacy
search_tool = Tool(
    name="search_web",
    func=search.run,
    description="Search the web for information"
)