🩺 AI Medical Assistant using RAG and Endee Vector Database
A production-style Retrieval-Augmented Generation (RAG) application that answers medical questions by retrieving relevant knowledge from a curated dataset stored in the Endee vector database, then generating a final answer via the Claude LLM.
📌 Project Overview
This project demonstrates how to build an end-to-end AI assistant using the RAG pattern — the gold-standard approach for grounding LLM responses in real, domain-specific knowledge rather than relying solely on training data.
The assistant is specialised for medical information: it can answer questions about symptoms, conditions, treatments, and when to see a doctor — all based on a curated knowledge base of 12 medical conditions.
🧩 Problem Statement
General-purpose LLMs (like GPT or Claude) are trained on broad internet data. For sensitive domains like medicine:
They may give outdated or hallucinated information
They lack source transparency (you don't know where the answer came from)
They cannot be easily updated with new or proprietary medical data
RAG solves this by keeping an external, updatable knowledge base and retrieving the most relevant pieces before generating any answer.
✅ Solution
Store a curated medical dataset as vector embeddings in Endee
When a user asks a question, embed the query and find the most semantically similar chunks in Endee
Pass the retrieved chunks as context to Claude
Claude generates a grounded, accurate answer based only on the retrieved information
🏗️ Architecture

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