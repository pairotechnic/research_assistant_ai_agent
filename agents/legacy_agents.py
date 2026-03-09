# Standard Library Imports
import json

# Third-Party Library Imports
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
# Legacy
from langchain_core.output_parsers import PydanticOutputParser
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor

# Local Application Imports
from tools.legacy_tools import search_tool

load_dotenv()

def legacy_agent(model, response_structure):

    llm = ChatOpenAI(model=model)

    parser = PydanticOutputParser(pydantic_object=response_structure)

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
