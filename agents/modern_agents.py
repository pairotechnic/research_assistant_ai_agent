# Standard Library Imports
import json

# Third-Party Library Imports
from dotenv import load_dotenv
# Modern
from langchain.agents import create_agent

# Local Application Imports
from tools.modern_tools import search_web

load_dotenv()

def modern_agent(model, response_format):
    # New Way
    tools = [search_web]
    agent = create_agent(
        model=model,
        tools=tools,
        response_format=response_format,
        system_prompt="""
            You are a research assistant that will help generate a research paper.
            Answer the user query and use necessary tools.
        """
    )
    
    query = input("What can I help you research?\n")


    stream = agent.stream(
        {
            "messages" : [
                {
                    "role" : "user",
                    "content" : query
                }
            ]
        },
        stream_mode = "updates"
    )

    final_structured_response = None

    for step in stream:
        print("\n--- AGENT STEP ---")
        print(json.dumps(step, indent=4, default=str))

        # capture final structured output
        if "structured_response" in step:
            final_structured_response = step["structured_response"]

    if final_structured_response:
        print("\n--- FINAL STRUCTURED RESPONSE ---")
        print(final_structured_response)

    # response = agent.invoke({
    #     "messages" : [
    #         {
    #             "role" : "user",
    #             "content" : query
    #         }
    #     ]
    # })

    # print(json.dumps(response["structured_response"], indent=4, default=dict))