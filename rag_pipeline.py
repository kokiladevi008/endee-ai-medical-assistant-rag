import os
from endee_db import EndeeDB
from utils import chunk_text
from anthropic import Anthropic


class RAGPipeline:
    def __init__(self):
        self.db = EndeeDB()
        self._load_data()

        self.client = None
        api_key = os.getenv("ANTHROPIC_API_KEY")

        if api_key:
            self.client = Anthropic(api_key=api_key)

    def _load_data(self):
        """Load medical dataset"""
        with open("data/medical_data.txt", "r", encoding="utf-8") as f:
            data = f.read()

        chunks = chunk_text(data)

        for chunk in chunks:
            self.db.add(chunk)

    def retrieve(self, query):
        return self.db.search(query, top_k=3)

    def generate_answer(self, query, context):
        """Call Claude if API key exists"""
        if not self.client:
            return None

        prompt = f"""
You are a medical assistant AI.

Use ONLY the context below to answer.

Context:
{chr(10).join(context)}

Question:
{query}

Answer clearly and simply:
"""

        message = self.client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=400,
            messages=[{"role": "user", "content": prompt}]
        )

        return message.content[0].text

    def run(self, query):
        context = self.retrieve(query)
        answer = self.generate_answer(query, context)

        return {
            "context": context,
            "answer": answer
        }
