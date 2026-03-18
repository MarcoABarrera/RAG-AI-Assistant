from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import os


DATA_PATH = "data"
DB_PATH = "db"


def load_documents():
    documents = []

    for file in os.listdir(DATA_PATH):
        if file.endswith(".pdf"):
            file_path = os.path.join(DATA_PATH, file)

            loader = PyPDFLoader(file_path)
            docs = loader.load()

            # Add metadata
            for doc in docs:
                doc.metadata["source"] = file
                doc.metadata["page"] = doc.metadata.get("page", 0)

            documents.extend(docs)

    print(f"Loaded {len(documents)} pages from PDFs")
    return documents


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)
    print(f"Split into {len(chunks)} chunks")

    return chunks


def create_vectorstore(chunks):
    embeddings = OpenAIEmbeddings()

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_PATH
    )

    vectordb.persist()
    print("✅ Vector DB created and persisted")


def run_ingestion():
    documents = load_documents()
    chunks = split_documents(documents)
    create_vectorstore(chunks)


if __name__ == "__main__":
    run_ingestion()