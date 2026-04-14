import numpy as np
from utils import get_embedding


class EndeeDB:
    def __init__(self):
        self.vectors = []
        self.texts = []

    def add(self, text):
        """Store text + embedding"""
        vector = get_embedding(text)

        self.vectors.append(vector)
        self.texts.append(text)

    def search(self, query, top_k=3):
        """Cosine similarity search"""
        query_vec = get_embedding(query)

        scores = []

        for i, vec in enumerate(self.vectors):
            score = self.cosine_similarity(query_vec, vec)
            scores.append((score, self.texts[i]))

        scores.sort(reverse=True, key=lambda x: x[0])

        top_results = [text for _, text in scores[:top_k]]

        return top_results

    def cosine_similarity(self, a, b):
        a = np.array(a)
        b = np.array(b)

        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
