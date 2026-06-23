# This code will not work because I do not have credits in OpenAI account.

from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.9)

response = llm.invoke("What is the capital of India?")

print(response)
