from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")

vector = embedding_model.embed_query("Which wizard could defeat Dumbledore?")

documents = ["Harry potter was a gifted wizard who studied in the Hogwarts school of witchcraft and wizardry.",
            "Lord Voldemort was a very powerful dark wizard who believed in the supremacy of pure-blood wizards and sought to conquer the wizarding world.",
            "Albus Dumbledore was a learned wizard and the only one who was able to defeat Lord Voldemort.",
            "Severus Snape was a skilled wizard who was a double agent for both Lord Voldemort and Albus Dumbledore."]

document_vectors = embedding_model.embed_documents(documents)

similarity_scores = cosine_similarity([vector], document_vectors)
sorted_documents_scores = sorted_pairs = sorted(enumerate(similarity_scores[0]), key=lambda x: x[1], reverse=True)
print("Most relevant documents:")
for index, score in sorted_documents_scores:
    print(f"Document: {documents[index]}, Similarity Score: {score}")
