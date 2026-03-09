# Standard Library Imports
import traceback
import json

# Third-Party Library Imports
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
# Legacy
from langchain_core.output_parsers import PydanticOutputParser
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
# Modern
from langchain.agents import create_agent

# Local Application Imports
from tools.legacy_tools import search_tool
from tools.modern_tools import search_web

load_dotenv()

class ResearchResponse(BaseModel):
    query: str
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

def naive_api_call(llm):
    try :
        response = llm.invoke("What is the meaning of life?")
        response_json = response.to_json()
        print(json.dumps(response_json, indent=4, default=str))
    except Exception as e:
        print(f"Error occurred during llm invoke : {str(e)}")
        print(traceback.format_exc())

def legacy_agent(llm):

    parser = PydanticOutputParser(pydantic_object=ResearchResponse)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
                You are a research assistant that will help generate a research paper.
                Answer the user query and use necessary tools.
                Wrap the output in this format and provide no other text\n{format_instructions}
                """,
            ),
            ("placeholder", "{chat_history}"),
            ("human", "{query}"),
            ("placeholder", "{agent_scratchpad}")
        ]
    ).partial(format_instructions=parser.get_format_instructions())
    
    tools = [search_tool]
    agent = create_tool_calling_agent(
        llm=llm,
        prompt=prompt,
        tools=tools
    )
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    query = input("What can I help you research?\n")
    raw_response = agent_executor.invoke({"query" : query})
    # print(json.dumps(raw_response, indent=4, default=dict))

    output = raw_response.get("output")
    print(json.dumps(json.loads(output), indent=4, default=str))

    # structured_response = parser.parse(output)
    # print(structured_response)
    # print(structured_response.topic)

def modern_agent():
    # New Way
    tools = [search_web]
    agent = create_agent(
        model="gpt-5-nano",
        tools=tools,
        response_format=ResearchResponse,
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


def main():
    llm = ChatOpenAI(model="gpt-5-nano")
    # naive_api_call(llm)
    # legacy_agent(llm)
    modern_agent()
    


if __name__ == "__main__":
    main()