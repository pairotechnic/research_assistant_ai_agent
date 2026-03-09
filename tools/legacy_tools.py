# Standard Library Imports
from datetime import datetime

# Third-Party Library Imports
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
# Legacy
from langchain_classic.tools import Tool

# Local Application Imports

search = DuckDuckGoSearchRun()

# Legacy
legacy_duck_duck_go_search_tool = Tool(
    name="search_web_using_duck_duck_go",
    func=search.run,
    description="Search the web for information using Duck Duck Go API"
)

wiki_api_wrapper = WikipediaAPIWrapper(top_k_results=5, doc_content_chars_max=1000)
legacy_wiki_search_tool = WikipediaQueryRun(api_wrapper=wiki_api_wrapper)

def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"

legacy_save_text_to_file_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Save structured research data to a text file"
)