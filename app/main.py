from fastapi import FastAPI, UploadFile, File
import shutil
import os

from app.rag.query import query_rag
from app.rag.ingest import run_ingestion

app = FastAPI()

DATA_PATH = "data"


@app.get("/")
def root():
    return {"message": "RAG AI Assistant is running 🚀"}


@app.post("/query")
def query(question: str):
    answer = query_rag(question)
    return {"question": question, "answer": answer}


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    file_path = os.path.join(DATA_PATH, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": f"{file.filename} uploaded successfully"}


@app.post("/ingest")
def ingest():
    run_ingestion()
    return {"message": "Documents ingested successfully"}