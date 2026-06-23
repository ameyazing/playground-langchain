from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chat_model1 = ChatGoogleGenerativeAI(model = "gemini-3.1-flash-lite", temperature = 0)
chat_model2 = ChatGoogleGenerativeAI(model = "gemini-3.1-flash-lite", temperature = 2.0)

result1 = chat_model1.invoke("Suggest 5 names for people")
result2 = chat_model2.invoke("Suggest 5 names for people")

print("Temperature 0.0")
print(result1.content[0].get('text'))
print("\nTemerature 2.0")
print(result2.content[0].get('text'))
