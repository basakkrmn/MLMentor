import os
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
import streamlit as st
import requests

# -----------------------------
# Load API keys from Streamlit secrets
# -----------------------------
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

# -----------------------------
# Settings
# -----------------------------
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
EMBEDDINGS_FILE = "embeddings.pkl"
TOP_K = 3

# -----------------------------
# Download embeddings.pkl from Google Drive if not exists
# -----------------------------
if not os.path.exists(EMBEDDINGS_FILE):
    file_id = "18Iq8-nyZa4aY091rfsm8WT9nODOYtFUF"  # Drive link ID
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    r = requests.get(url)
    with open(EMBEDDINGS_FILE, "wb") as f:
        f.write(r.content)

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
        model = genai.GenerativeModel('models/gemini-2.0-flash-lite')
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.1,
                max_output_tokens=1000
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
            if relevant_chunks:
                return f"Based on available information:\n\n{relevant_chunks[0][:800]}..."
            else:
                return "I couldn't find relevant information in my knowledge base to answer this question."
