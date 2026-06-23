from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
image_model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-image")

# 'human', 'user', 'ai', 'assistant', 'function', 'tool', 'system', or 'developer' are all valid roles for the chat history. The model will use these roles to understand the context of the conversation and generate appropriate responses. Internally langchain will convert 'human' to HumanMessage, 'ai' to AIMessage, and so on, but you can use the string versions for simplicity.
chat_history = [
    ("system", "You are a assistant that gives the code for the Arduino based on the instructions")
]

# Set the page title
st.title("Arduino Assistant")
user_input = st.text_input("Type your message here:")

if st.button("Send"):
    st.write("You entered:", user_input)
    chat_history.append(("user", user_input))
    response = chat_model.invoke(chat_history)
    chat_history.append(("ai", response.content[0].get("text")))
    st.write("AI Response: ", response.content[0].get("text"))

things = [response.content[0].get("text")]
class Things(BaseModel):
    components = list[str] = Field(description = "A list of things that are needed for the project")
    steps = list[str]  = Field(description = "A list of steps to connect the various parts of the circuit together")


prompt = PromptTemplate(
    template = "Give me the components which is a list of things that are needed for the project, and a list of steps to connect the various parts of the circuit together. These are the details: {user_input}.",
    input_variables = ["user_input"]
)
structured_model = chat_model.with_structured_output(Things)

chain = prompt | structured_model
result = chain.invoke({"user_input": user_input})
