
from langchain.chains import RetrievalQA
from langchain_ollama import ChatOllama
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


def load_rag_pipeline(persist_dir="db"):
    # Step 1: Load retriever (Chroma)
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = Chroma(
        collection_name="faq_chunks",
        embedding_function=embedding,
        persist_directory=persist_dir
    )

    # Step 2: Setup LLM
    llm = ChatOllama(model="gemma:2b")

    # Step 3: Create RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectordb.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True
    )

    return qa_chain
