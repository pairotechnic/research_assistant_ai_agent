# Standard Library Imports
import json

# Third-Party Library Imports
from dotenv import load_dotenv
# Modern
from langchain.agents import create_agent

# Local Application Imports
from tools.modern_tools import search_web

load_dotenv()

def modern_agent(model, response_structure):
    # New Way
    tools = [search_web]
    agent = create_agent(
        model=model,
        tools=tools,
        response_format=response_structure,
        system_prompt="""
            You are a research assistant that will help generate a research paper.
            Answer the user query and use necessary tools.
        """
    )
    
    query = input("What can I help you research?\n")
    response = agent.invoke({
        "messages" : [
            {
                "role" : "user",
                "content" : query
            }
        ]
    })

    print(json.dumps(response["structured_response"], indent=4, default=dict))
