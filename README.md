# 📄 DocuBot

DocuBot is an AI-powered document chatbot that lets you upload PDF files and ask questions directly from them. It uses NLP to extract content, generate embeddings, and return context-aware answers.

---

## 🚀 Features

- 📂 Upload PDF files
- 🧠 Ask natural language questions
- 📌 Context-aware answers using RAG (Retrieval-Augmented Generation)
- 🧾 View source chunks used for responses
- 🔧 Simple frontend in HTML, CSS, JS

---

## 🛠️ Tech Stack

- **Backend:** FastAPI, LangChain, ChromaDB, OpenAI/Ollama
- **Parsing:** pdfplumber / PyMuPDF
- **Embeddings:** Sentence-Transformers (`all-MiniLM-L6-v2`)
- **Frontend:** HTML, CSS, JavaScript
- **Storage (optional):** MongoDB (for logs)

---

## 📦 Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/docubot.git
cd docubot

python -m venv venv
venv\Scripts\activate   # For Windows
# or
source venv/bin/activate   # For Linux/macOS

pip install -r requirements.txt

OPENAI_API_KEY=your-api-key-here

uvicorn main:app --reload

