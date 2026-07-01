import os

# --- PREVENT ALL EXTERNAL NETWORK CONNECTIONS ---
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"
# ------------------------------------------------

import json
from langchain_core.documents import Document
from langchain_unstructured import UnstructuredLoader


def load_document(path):
    """Loads scanned PDFs completely offline using the 'ocr_only' strategy.

    This bypasses complex deep-learning vision architectures entirely.
    """
    loader = UnstructuredLoader(
        file_path=path,
        strategy="ocr_only",  # <-- FORCES DIRECT LOCAL TESSERACT OCR SCANNING
        languages=["eng"],
    )
    return loader.load()


def save_docs_to_cache(docs, cache_path):
    """Serializes LangChain Document objects into a local JSON file."""
    serialized_data = [
        {"page_content": doc.page_content, "metadata": doc.metadata}
        for doc in docs
    ]
    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(serialized_data, f, ensure_ascii=False, indent=4)
    print(f"--> Saved {len(docs)} chunks safely to disk cache: {cache_path}")


def load_docs_from_cache(cache_path):
    """Deserializes a local JSON file back into LangChain Document objects."""
    with open(cache_path, "r", encoding="utf-8") as f:
        serialized_data = json.load(f)
    print(f"--> Loaded chunks instantly from disk cache: {cache_path}")
    return [
        Document(
            page_content=item["page_content"], metadata=item["metadata"]
        )
        for item in serialized_data
    ]


if __name__ == "__main__":
    books = [{"name": "textbook_class08_chemistry.pdf"}]

    scriptdir = os.path.dirname(os.path.abspath(__file__))
    cache_dir = os.path.join(scriptdir, "cache")
    os.makedirs(cache_dir, exist_ok=True)

    all_docs = []

    for book in books:
        bookpath = os.path.join(scriptdir, "books", book["name"])

        # Create a valid cache filename
        base_name = os.path.splitext(book["name"])[0]
        cache_path = os.path.join(cache_dir, f"{base_name}_cache.json")

        if os.path.exists(cache_path):
            print(f"Found cache for {book['name']}. Skipping OCR...")
            book_docs = load_docs_from_cache(cache_path)
            all_docs.extend(book_docs)
        elif os.path.exists(bookpath):
            print(
                f"Processing local offline OCR on: {book['name']} (OCR Only mode)..."
            )
            try:
                book_docs = load_document(bookpath)
                save_docs_to_cache(book_docs, cache_path)
                all_docs.extend(book_docs)
            except Exception as e:
                print(f"Failed to parse {book['name']}. Error: {e}")
        else:
            print(f"Error: Raw file not found at '{bookpath}'")

    print(
        f"\nProcessing Complete. Total scanned text chunks available: {len(all_docs)}"
    )
    if all_docs:
        print("\nDisplaying samples of extracted text:")
        for idx, doc in enumerate(all_docs[:5]):
            clean_content = doc.page_content[:60].replace("\n", " ").strip()
            if clean_content:
                print(f"Chunk {idx + 1}: {clean_content}...")
