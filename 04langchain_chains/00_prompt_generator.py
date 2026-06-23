from langchain_core.prompts import PromptTemplate
from langchain_core.load import dumps

# Create a prompt template
prompt_detailed_report_template = PromptTemplate(
    template="Generate a detailed report on **{topic}**",
    input_variables=["topic"]
)

prompt_summarize_report_template = PromptTemplate(
    template="Create a short summary of below detailed report on **{topic}**:\n\n{detailed_report}",
    input_variables=["topic", "detailed_report"]
)

serialized_prompt = dumps(prompt_detailed_report_template, pretty=True)
file_path = ".\\04langchain_chains\\detailed_report.json"
with open(file_path, "w", encoding="utf-8") as f:
    f.write(serialized_prompt)

serialized_prompt = dumps(prompt_summarize_report_template, pretty=True)
file_path = ".\\04langchain_chains\\summarize.json"
with open(file_path, "w", encoding="utf-8") as f:
    f.write(serialized_prompt)

