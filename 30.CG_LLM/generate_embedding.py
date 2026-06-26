import requests
import json
import os
from sklearn.metrics.pairwise import cosine_similarity

def create_embeddings(text, api_key, model="amazon.titan-embed-text-v2:0"):
    url = "https://openai.generative.engine.capgemini.com/v1/embeddings"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "input": text,
        "model": model
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        
        # Return single embedding or list based on input
        if isinstance(text, str):
            return result['data'][0]['embedding']
        else:
            return [item['embedding'] for item in result['data']]
            
    except Exception as err:
        print(f"Error occurred: {err}")
        return None

# Example usage
if __name__ == "__main__":
    api_key = os.environ.get("CAPGEMINI_GENAI_API_KEY")
    if not api_key:
        raise RuntimeError("API Key not found. Please check if CAPGEMINI_GENAI_API_KEY variable is correctly set")

    # Single text embedding
    query = "Who is the most powerful wizard?"
    query_vector = create_embeddings(query, api_key)
    
    # Multiple texts embedding
    docs = [
        "Harry Potter: The courageous and determined \"Boy Who Lived\" who overcame immense trauma to defeat Lord Voldemort and unite the wizarding world.",
        "Albus Dumbledore: The brilliant, enigmatic, and beloved Headmaster of Hogwarts who guided Harry and served as the greatest obstacle to the Dark Arts.",
        "Severus Snape: The complex, formidable Potions Master whose bitter exterior concealed unwavering bravery, lifelong loyalty, and dedication to defeating Voldemort.",
        "Lord Voldemort: The terrifying, megalomaniacal dark wizard obsessed with blood purity and immortality, whose ruthless actions caused decades of war and suffering.",
        "Hermione Granger: The fiercely intelligent, Muggle-born witch whose exceptional intellect, resourcefulness, and ethical convictions were vital to Harry's survival.",
        "Merlin: The legendary, elusive enchanter of Arthurian myth, heavily praised in magical history for his immense knowledge and influence on early wizarding governance.",
        "Gandalf: The wise, wandering wizard and Maiar whose humility and strategic council rallied the Free Peoples of Middle-earth against Sauron.",
        "Gellert Grindelwald: A charismatic and formidable dark wizard whose pursuit of the Deathly Hallows and wizarding supremacy sparked a global revolution.",
        "Salazar Slytherin: A cunning, medieval wizard and Hogwarts Founder who championed pure-blood supremacy and created the hidden Chamber of Secrets.",
        "Godric Gryffindor: A brave, chivalrous Hogwarts Founder who passionately advocated for Muggle-born students and wielded an iconic, goblin-made sword."
    ]
    doc_vectors = create_embeddings(docs, api_key)

similarity_scores = cosine_similarity([query_vector], doc_vectors)
indexed_similarity_scores = list(enumerate(similarity_scores[0]))
sorted_similarity_scores = sorted(indexed_similarity_scores, key=(lambda x: x[1]), reverse=True)
print(sorted_similarity_scores)
