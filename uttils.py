from sentence_transformers import SentenceTransformer
import numpy as np

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding(text: str):
    """Convert text → vector embedding"""
    return model.encode(text)


def chunk_text(text, chunk_size=300):
    """Simple text splitter"""
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks
