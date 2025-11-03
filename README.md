# 🧠 ML Mentor
**RAG-based Machine Learning Chatbot for Akbank GenAI Bootcamp**

This project provides a web interface to interact with a chatbot that answers questions about machine learning topics using retrieval-augmented generation.

---

## 📋 Project Overview
ML Mentor is a Machine Learning assistant that allows users to ask questions about ML topics.  
The chatbot uses **RAG (Retrieval-Augmented Generation)** to find relevant information from prepared Markdown files and generate informative answers using the Google Gemini API.

**Key Features:**
- Searchable knowledge base built from Markdown files
- Embeddings with Sentence Transformers (`all-MiniLM-L6-v2`)
- Question answering via Google Gemini model
- Interactive web interface with Streamlit

---

## 🛠️ Technologies Used
- **RAG pipeline:** Custom implementation with embeddings and Google Gemini
- **Embedding model:** `sentence-transformers/all-MiniLM-L6-v2`
- **Generation model:** Google Gemini 2.0 (flash-lite)
- **Web framework:** Streamlit
- **Vector store:** Pickle-based in-memory storage
- **Environment variables management:** python-dotenv

---

## 📁 Project Structure
```
MLMentor/
├── data/ # Markdown documents used for RAG
│ ├── Feature_Engineering.md
│ ├── Model_Evaluation.md
│ ├── Natural_Language_Processing.md
│ ├── Neural_Networks.md
│ ├── Supervised_Learning.md
│ └── Unsupervised_Learning.md
├── src/
│ ├── chatbot.py # Core chatbot logic
│ ├── ingest.py # Embedding creation
│ └── _init_.py
├── embeddings.pkl # Precomputed embeddings
├── streamlit_chatbot.py # Streamlit interface
├── .env # API keys (do NOT commit)
├── requirements.txt
└── README.md
```

---

## 🚀 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/basakkrmn/MLMentor.git
cd MLMentor
```
### 2. Create and activate a virtual environment (optional but recommended)
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Set up environment variables
Create a .env file in the project root:
```.env
GEMINI_API_KEY=your_gemini_api_key_here
```
### 5. Create embeddings
```bash
python src/ingest.py
```
### 6. Run the Streamlit app
```bash
streamlit run streamlit_chatbot.py
```
The web app will open automatically (default: http://localhost:8501).
## 💡 How it Works

**Data Loading:** Markdown files are loaded from the data/ folder.

**Embedding:** Each document is converted into a vector using SentenceTransformer.

**Vector Store:** Embeddings are saved to embeddings.pkl for quick retrieval.

**Querying:** User questions are converted to embeddings and the top relevant documents are retrieved.

**Answer Generation:** Google Gemini model generates a clear, structured answer based on retrieved context.

## 🎯 Example Questions

What is supervised learning?

How do neural networks work?

Explain cross-validation with an example

What are feature engineering techniques?

## ⚠️ Notes

First run will compute embeddings; this may take a few minutes.

Make sure your GEMINI API key has sufficient quota.

Streamlit cache ensures faster subsequent runs.

## Demo

You can try the deployed app here: [ML Mentor Chatbot](https://mlmentor-r6usqtnevvrrektgiocf9p.streamlit.app/)

⚠️ **Note:** The app runs on Streamlit Community Cloud free tier. If inactive for 18+ hours, it enters sleep mode. The first visit may take 30-60 seconds to wake up.

## 📝 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 🤝 Contribution

Feel free to open issues for questions, bugs, or suggestions.
