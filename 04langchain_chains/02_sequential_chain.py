from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableMap
from langchain_core.load import loads
from pydantic import BaseModel, Field
import warnings
from langchain_core._api import LangChainBetaWarning
from dotenv import load_dotenv
import json

warnings.simplefilter("ignore", category=LangChainBetaWarning)

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model = "gemini-3.1-flash-lite", temperature = 0.9)

with open(".\\04langchain_chains\\detailed_report.json", "r", encoding="utf-8") as f:
    prompt_detailed_report_template = loads(f.read())

with open(".\\04langchain_chains\\summarize.json", "r", encoding="utf-8") as f:
    prompt_summarize_template = loads(f.read())

class DetailedReport(BaseModel):
    topic: str = Field(description="return the topic provided by the user as-is")
    detailed_report: str = Field(description="provide a detailed report on the topic mentioned by the user")

structured_model_detailed_report = chat_model.with_structured_output(DetailedReport)

class ReportSummary(BaseModel):
    topic: str = Field(description="return the topic provided by the user as-is")
    summary: list[str] = Field(description="Summary of the detailed report in 3 bullet points")

structured_model_summary = chat_model.with_structured_output(ReportSummary)

chain = (
    prompt_detailed_report_template
    | structured_model_detailed_report
    | (lambda output: {'topic': output.topic, 'detailed_report': output.detailed_report})
    | prompt_summarize_template
    | structured_model_summary
)

try:
    response = chain.invoke({"topic": "Dhurandhar (2025) movie franchise"})
    for x in range(3):
        print(response.summary[x])
except Exception as e:
    # Read the text name of the exception class safely
    error_type = e.__class__.__name__
    if error_type in ["ServerError", "APIError"] or "503" in str(e):
        print("\n❌ Gemini API is currently unavailable due to high demand.")
        print("Please wait a moment and try running your script again.")
    else:
        print(f"\n❌ A different error occurred ({error_type}): {e}")
