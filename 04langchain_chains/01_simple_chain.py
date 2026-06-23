from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

class FactList(BaseModel):
    topic: str = Field(description="The topic to generate facts about")
    facts: list[str] = Field(description="List of facts about the topic")

prompt = PromptTemplate(
    template = "Generate 5 interesting facts about {topic}.",
    input_variables = ["topic"]
)

chat_model = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0.9)
structured_model = chat_model.with_structured_output(FactList)

chain = prompt | structured_model
result = chain.invoke({"topic": "space exploration"})

print(result)
