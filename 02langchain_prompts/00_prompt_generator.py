from langchain_core.prompts import PromptTemplate

# Create a prompt template
prompt_template = PromptTemplate(
    template="Tell me about {character} in a {length} and {style} way.",
    input_variables=["character", "length", "style"]
)

prompt_template.save(".\\02langchain_prompts\\hp_character_summary_prompt.json")
