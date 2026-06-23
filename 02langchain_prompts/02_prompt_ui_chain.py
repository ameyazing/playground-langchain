# This code is identical to 01_prompt_ui.py, but demonstrates how to chain prompt creation and execution together in a single invoke call.
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.load import loads
from dotenv import load_dotenv
import streamlit as st
import json

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

# Streamlit UI
st.header("Welcome to Hogwards School of Witchcraft and Wizardry!")
character_input = st.selectbox("Select a character to ask questions about:", ["Harry Potter", "Lord Voldemort", "Albus Dumbledore", "Severus Snape"])
length_input = st.selectbox("Select the length of the response:", ["Short", "Medium", "Long"])
style_input = st.selectbox("Select the style of the response:", ["Formal", "Informal", "Humorous"])

# Create the prompt
prompt_dict = {}
with open("hp_character_summary_prompt.json", "r", encoding="utf-8") as f:
    prompt_dict = json.load(f)
prompt_template = PromptTemplate(template=prompt_dict["template"], input_variables=["character", "length", "style"])

# Execute the prompt and display the response
if st.button("Ask"):
    #Instead of creating the prompt and then invoking the model separately, we can chain them together using the | operator.
    chain = prompt_template | chat_model
    response = chain.invoke({"character": character_input, "length": length_input, "style": style_input})
    st.write("Response: ", response.content[0].get("text"))
