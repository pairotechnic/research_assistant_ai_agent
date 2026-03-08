from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
import traceback
import json

load_dotenv()

llm = ChatOpenAI(model="gpt-5-nano")

try :
    response = llm.invoke("What is the meaning of life?")
    response_json = response.to_json()
    print(json.dumps(response_json, indent=4, default=str))
except Exception as e:
    print(f"Error occurred during llm invoke : {str(e)}")
    print(traceback.format_exc())