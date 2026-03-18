from dotenv import load_dotenv
import os

load_dotenv()

from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama


DB_PATH = "db"


def query_rag(question: str):
    # 1. Load embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    # 2. Load vector DB
    vectordb = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embeddings
    )

    # 3. Retrieve relevant chunks
    retriever = vectordb.as_retriever(search_kwargs={"k": 6}) #more chunks better answers
    docs = retriever.invoke(question)

    print("\n🔎 Retrieved context:\n")
    for doc in docs:
        print(f"- {doc.metadata['source']} (page {doc.metadata['page']})")

    # 4. LLM
    llm = ChatOllama(model="llama3")

    # 5. Build prompt
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
    You are an AI assistant helping with machine learning concepts.

    Use ONLY the provided context to answer clearly and concisely.
    If the answer is not in the context, say "I don't know".

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    # 6. Generate answer
    response = llm.invoke(prompt)

    return response.content


if __name__ == "__main__":
    question = input("Ask a question: ")
    answer = query_rag(question)
    print("\n💡 Answer:\n", answer)