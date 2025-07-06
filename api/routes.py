# api/routes.py
from fastapi import APIRouter, UploadFile, File
from fastapi import HTTPException
from pydantic import BaseModel
import os

from utils.pdf_parser import extract_text_from_pdf
from utils.chunker import chunk_text
from services.embedding_service import generate_embeddings
from services.vector_store import create_chroma_store, add_documents, search_similar
from services.rag_pipeline import load_rag_pipeline
from services.db import uploads_collection
from services.db import queries_collection

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        # Save temporarily
        save_path = f"data/{file.filename}"
        with open(save_path, "wb") as f:
            content = await file.read()
            f.write(content)

        # Process document
        text = extract_text_from_pdf(save_path)
        chunks = chunk_text(text)
        metadatas = [{"source": file.filename, "chunk_id": i} for i in range(len(chunks))]

        # Store in Chroma
        db = create_chroma_store()
        add_documents(db, chunks, metadatas)

        #set MONGO for logging
        uploads_collection.insert_one({
            "file_name": file.filename,
            "num_chunks": len(chunks),
            "metadatas": metadatas
        })
        print({"message": f"Uploaded and stored {len(chunks)} chunks."})
        return {"message": f"Uploaded and stored {len(chunks)} chunks."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/query")
async def ask_question(body: QueryRequest):
    try:
        qa_chain = load_rag_pipeline()
        result = qa_chain.invoke({"query": body.question})

        # Get source docs for logging
        sources = [doc.metadata for doc in result['source_documents']]

        queries_collection.insert_one({
            "question": body.question,
            "sources": sources,
            "response": result["result"]
        })

        return {
            "question": body.question,
            "answer": result["result"],
            "sources": [doc.metadata for doc in result["source_documents"]],
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
