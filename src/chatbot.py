import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
from dotenv import load_dotenv
import os
import time

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY is None:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# -----------------------------
# Settings
# -----------------------------
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
EMBEDDINGS_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "../embeddings.pkl"))
TOP_K = 3

# -----------------------------
# Load embeddings and configure Gemini
# -----------------------------
with open(EMBEDDINGS_FILE, "rb") as f:
    embeddings_data = pickle.load(f)

embedding_model = SentenceTransformer(EMBEDDING_MODEL)
genai.configure(api_key=GEMINI_API_KEY)


# -----------------------------
# Helper functions
# -----------------------------
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


def retrieve_relevant_chunks(query, top_k=TOP_K):
    query_emb = embedding_model.encode(query)
    similarities = []
    for item in embeddings_data:
        sim = cosine_similarity(query_emb, item["embedding"])
        similarities.append((sim, item["text"]))
    similarities.sort(key=lambda x: x[0], reverse=True)
    return [text for _, text in similarities[:top_k]]


# -----------------------------
# Chatbot function
# -----------------------------
def ask_chatbot(question):
    relevant_chunks = retrieve_relevant_chunks(question)
    context = "\n".join(relevant_chunks)

    prompt = f"""
You are an expert Machine Learning assistant. Use the provided context to answer the question accurately and informatively.

Context:
{context}

Question: {question}

Instructions:
- Answer based only on the provided context
- If the context doesn't contain relevant information, say so
- Keep the answer clear and structured
- Use technical terms appropriately

Answer:
"""
    try:
        # Use lightweight model to save quota
        model = genai.GenerativeModel('models/gemini-2.0-flash-lite')
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.1,  # Lower temperature for more consistent answers
                max_output_tokens=1000  # Limit tokens to save quota
            )
        )
        return response.text

    except Exception as e:
        error_msg = str(e)
        if "quota" in error_msg.lower() or "429" in error_msg:
            return "⚠️ Sorry, I've reached the API rate limit. Please try again in a few minutes."
        elif "503" in error_msg:
            return "🔧 Service temporarily unavailable. Please try again shortly."
        else:
            # Fallback: return most relevant chunk
            if relevant_chunks:
                return f"Based on available information:\n\n{relevant_chunks[0][:800]}..."
            else:
                return "I couldn't find relevant information in my knowledge base to answer this question."