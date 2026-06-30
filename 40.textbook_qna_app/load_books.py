from langchain_unstructured import UnstructuredLoader

def load_document(path):
    loader = UnstructuredLoader(path)
    docs = loader.load()
    print(f"total docs = {len(docs)}")
    return docs[0]

