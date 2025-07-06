# test_vectorstore.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from utils.pdf_parser import extract_text_from_pdf
from utils.chunker import chunk_text
from services.embedding_service import generate_embeddings
from services.vector_store import create_chroma_store, add_documents, search_similar

file_path = r"data\sample.pdf"
text = extract_text_from_pdf(file_path)
chunks = chunk_text(text)

# Simple metadata per chunk (can expand later)
metadatas = [{"source": file_path, "chunk_id": i} for i in range(len(chunks))]

# Create Chroma store
chroma = create_chroma_store()

# Add chunks
add_documents(chroma, chunks, metadatas)

# Try a similarity search
results = search_similar(chroma, query=" Success is the result of ?", k=3)

for i, res in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(res.page_content)
    print("Metadata:", res.metadata)
