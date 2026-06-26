from langchain_openai import ChatOpenAI
import os

def create_model(api_key):
    model = ChatOpenAI(
        model="anthropic.claude-sonnet-4-6",  # Anthropic model
        base_url="https://openai.generative.engine.capgemini.com/v1",
        api_key=api_key,
    )
    return model

def call_llm(prompt, api_key):
    model = create_model(api_key)
    response = model.invoke(prompt)
    return response

if __name__ == "__main__":
    api_key = os.environ.get("CAPGEMINI_GENAI_API_KEY")
    if not api_key:
        raise RuntimeError("API Key not found. Please check if CAPGEMINI_GENAI_API_KEY variable is correctly set")

    prompt = "What is the capital of India?"

    response = call_llm(prompt, api_key)

    print(response.content)
