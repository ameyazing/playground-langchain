from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

# 'human', 'user', 'ai', 'assistant', 'function', 'tool', 'system', or 'developer' are all valid roles for the chat history. The model will use these roles to understand the context of the conversation and generate appropriate responses. Internally langchain will convert 'human' to HumanMessage, 'ai' to AIMessage, and so on, but you can use the string versions for simplicity.
chat_history = [
    ("system", "You are a helpful assistant that provides information about Hogwarts School of Witchcraft and Wizardry.")
]

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    chat_history.append(("user", user_input))
    response = chat_model.invoke(chat_history)
    chat_history.append(("ai", response.content[0].get("text")))
    print("AI Response: ", response.content[0].get("text"))

print(chat_history)
