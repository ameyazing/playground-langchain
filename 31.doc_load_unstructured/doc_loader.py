from langchain_unstructured import UnstructuredLoader

def load_document(path):
    loader = UnstructuredLoader(path)
    docs = loader.load()
    print(f"total docs = {len(docs)}")
    return docs[0]

if __name__ == "__main__":
    text_doc = load_document(".\\10.doc_load_split_store_retrieve\\docs\\a-testament-of-hope.pdf")
    print(type(text_doc.page_content[:200]))
