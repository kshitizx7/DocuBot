from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def generate_embeddings(chunks: list[str]) -> list[list[float]]:
    return embedding_model.embed_document(chunks)

