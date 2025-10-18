import os
import pickle
from sentence_transformers import SentenceTransformer

# -----------------------------
# Settings
# -----------------------------
DATA_DIR = "../data"
EMBEDDINGS_FILE = "../embeddings.pkl"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# -----------------------------
# Read Markdown files
# -----------------------------
print("Reading Markdown files...")
md_files = []
for root, dirs, files in os.walk(DATA_DIR):
    for file in files:
        if file.endswith(".md"):
            md_files.append(os.path.join(root, file))

documents = []
for file_path in md_files:
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read().strip()
        if text:  # skip empty files
            documents.append({"text": text})

print(f"Found {len(documents)} documents.")

# -----------------------------
# Create embeddings
# -----------------------------
print("Creating embeddings...")
model = SentenceTransformer(EMBEDDING_MODEL)
for doc in documents:
    doc["embedding"] = model.encode(doc["text"])

# -----------------------------
# Save embeddings
# -----------------------------
print(f"Saving embeddings to {EMBEDDINGS_FILE}...")
with open(EMBEDDINGS_FILE, "wb") as f:
    pickle.dump(documents, f)

print("Done!")