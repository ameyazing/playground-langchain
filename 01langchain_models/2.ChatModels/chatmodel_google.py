from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
response = chat_model.invoke("What is the financial capital of India?")
print(response.content[0].get("text"))
