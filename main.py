# Standard Library Imports
import traceback
import json

# Third-Party Library Imports
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI

# Local Application Imports
from agents.legacy_agents import legacy_agent
from agents.modern_agents import modern_agent

load_dotenv()

class ResearchResponse(BaseModel):
    query: str
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

def naive_api_call(model):
    llm = ChatOpenAI(model=model)
    try :
        response = llm.invoke("What is the meaning of life?")
        response_json = response.to_json()
        print(json.dumps(response_json, indent=4, default=str))
    except Exception as e:
        print(f"Error occurred during llm invoke : {str(e)}")
        print(traceback.format_exc())

def main():
    model="gpt-5-nano"
    naive_api_call(model)
    legacy_agent(model=model, response_fomat=ResearchResponse)
    modern_agent(model, response_format=ResearchResponse)
    
if __name__ == "__main__":
    main()