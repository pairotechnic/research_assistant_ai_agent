# Standard Library Imports
from datetime import datetime

# Third-Party Library Imports
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
# Modern
from langchain.tools import tool

# Local Application Imports

search = DuckDuckGoSearchRun()

# Modern
@tool
def modern_duck_duck_go_search_tool(query: str) -> str:
    """Search the web for information using Duck Duck Go API"""
    return search.run(query)

# Wiki tool is still used the same way
wiki_api_wrapper = WikipediaAPIWrapper(top_k_results=5, doc_content_chars_max=1000)
modern_wiki_search_tool = WikipediaQueryRun(api_wrapper=wiki_api_wrapper)

@tool
def modern_save_text_to_file_tool(data: str, filename: str = "research_output.txt"):
    "Save structured research data to a text file"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"