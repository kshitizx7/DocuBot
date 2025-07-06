from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
import os

# Initialize embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# what does create_chroma_store function do
# Make me a Chroma database that saves files in the db/ folder,
# uses the HuggingFace model to understand text,
# and organizes it under the name faq_chunks.

def create_chroma_store(persist_directory="db", collection_name="faq_chunks"):
    return Chroma(
        collection_name=collection_name,
        embedding_function=embedding_model,
        persist_directory=persist_directory
    )

# It creates a list of LangChain Document objects, where each document contains:
# The actual text (called page_content)
# Some extra information about that text (called metadata)
def add_documents(chroma, chunks: list[str], metadatas: list[dict]):
    docs = [Document(page_content=c, metadata=m) for c, m in zip(chunks, metadatas)]
    chroma.add_documents(docs)

#“Given this question, 
#Find the top 3 chunks from the database that are most closely related in meaning.”

def search_similar(chroma, query: str, k: int = 3):
    return chroma.similarity_search(query, k=k)
