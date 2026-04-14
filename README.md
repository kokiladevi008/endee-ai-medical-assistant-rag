
# 🩺 AI Medical Assistant using RAG 

An AI-powered medical assistant that uses Retrieval-Augmented Generation (RAG) to provide accurate, context-based answers by retrieving relevant medical knowledge from a vector database (Endee) and generating responses using Claude LLM.

---

## 🚀 Features
- 🔍 Semantic search using embeddings
- 🧠 RAG-based response generation
- 🗄️ Endee vector database for storage
- 🤖 Claude LLM for final answer generation
- 💬 Streamlit web interface
- 📚 Curated dataset of 12 medical conditions

---

## 🧩 How It Works
1. User enters a medical question  
2. Query is converted into embeddings  
3. Endee performs similarity search  
4. Relevant medical context is retrieved  
5. Context + query sent to Claude  
6. AI generates final grounded answer  

---

## 🏗️ Architecture
User → Embedding Model → Endee Vector DB → Context Retrieval → Claude LLM → Answer → Streamlit UI

---

## 📦 Tech Stack
- Streamlit  
- Sentence Transformers (all-MiniLM-L6-v2)  
- Endee Vector Database  
- Anthropic Claude API  
- Python  

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/ai-medical-assistant
cd ai-medical-assistant
pip install -r requirements.txt

## Flow chart

User Question
     │
     ▼
┌─────────────────┐
│  Embed Query    │  ← sentence-transformers (all-MiniLM-L6-v2)
└────────┬────────┘
         │ query vector
         ▼
┌─────────────────────────────────┐
│         Endee Vector DB         │  ← cosine similarity search
│  (12 medical condition chunks)  │
└────────┬────────────────────────┘
         │ top-k relevant chunks
         ▼
┌─────────────────────────────────┐
│   Prompt = Context + Question   │
└────────┬────────────────────────┘
         │
         ▼
┌─────────────────┐
│   Claude LLM    │  ← Anthropic API (claude-3-haiku)
└────────┬────────┘
         │
         ▼
    Final Answer  →  Streamlit UI