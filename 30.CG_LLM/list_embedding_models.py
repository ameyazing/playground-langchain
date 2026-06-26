import requests
import os

api_key = os.environ.get("CAPGEMINI_GENAI_API_KEY")
if not api_key:
    raise RuntimeError("API Key not found. Please check if CAPGEMINI_GENAI_API_KEY variable is correctly set")

def get_embedding_models(api_key):
    url = "https://openai.generative.engine.capgemini.com/v1/embeddings/models"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as err:
        print(f"Error occurred: {err}")
        return None

# Usage
models = get_embedding_models(api_key)
print(models)
