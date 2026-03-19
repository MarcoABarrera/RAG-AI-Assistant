# RAG AI Assistant for Technical Documents

An end-to-end **Retrieval-Augmented Generation (RAG)** system that allows users to upload PDFs and query them using a fully local AI pipeline.

---

##  Features

*  Upload and process multiple PDF documents
*  Semantic search using vector embeddings
*  Context-aware question answering
*  FastAPI backend with REST endpoints
*  Dockerized for easy deployment
*  Fully local (no API costs)

---

##  Architecture

```
PDFs → Chunking → Embeddings → Vector DB (Chroma)
                                      ↓
User Query → Retrieval → Local LLM (Ollama) → Answer
```

---

##  Tech Stack

* **Backend:** FastAPI
* **LLM:** Ollama (Mistral / LLaMA3)
* **Embeddings:** HuggingFace (MiniLM)
* **Vector DB:** Chroma
* **Framework:** LangChain
* **Containerization:** Docker

---

##  Project Structure

```
rag-ai-assistant/
│
├── app/
│   ├── main.py          # FastAPI app
│   ├── rag/
│   │   ├── ingest.py    # PDF ingestion pipeline
│   │   └── query.py     # RAG query pipeline
│
├── data/                # Uploaded PDFs
├── db/                  # Vector database
├── Dockerfile
├── requirements.txt
├── .env.example
└── README.md
```

---

##  Setup (Local)

### 1. Clone repo

```
git clone https://github.com/yourusername/rag-ai-assistant.git
cd rag-ai-assistant
```

### 2. Create environment

```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run API

```
uvicorn app.main:app --reload
```

---

##  API Endpoints

### 🔹 Query

```
POST /query
```

**Request:**

```json
{
  "question": "Explain gradient descent"
}
```

---

### 🔹 Upload PDF

```
POST /upload
```

---

### 🔹 Ingest Documents

```
POST /ingest
```

---

## 🐳 Run with Docker

### Build image

```
docker build -t rag-ai .
```

### Run container

```
docker run -p 8000:8000 rag-ai
```

---

##  Local LLM Setup (Ollama)

Install Ollama and pull a model:

```
ollama pull mistral
```

Ensure Ollama is running before querying.

---

##  Key Highlights

* Designed a **scalable RAG pipeline** for document understanding
* Implemented **hallucination control** (answers strictly based on context)
* Migrated from API-based embeddings to **fully local architecture**
* Containerized the system for **production-ready deployment**

---

##  Future Improvements

* Streamlit App
* Authentication & user sessions
* Docker Compose (API + Ollama)
* GPU acceleration

---

## 👤 Author

**Marco Antonio Barrera Salas**
Data Engineer | Data Scientist

* [LinkedIn](https://www.linkedin.com/in/marcobarrera98/)
* [GitHub](https://github.com/MarcoABarrera)

---

## ⭐️ If you like this project

Give it a star ⭐ and feel free to contribute!
