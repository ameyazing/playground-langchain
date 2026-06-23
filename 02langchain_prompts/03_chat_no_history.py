from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chat_model.invoke(user_input)
    print("AI Response: ", response.content[0].get("text"))
