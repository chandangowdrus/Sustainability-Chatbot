import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai
from sentence_transformers import SentenceTransformer
import faiss
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Load local embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Streamlit UI setup
st.set_page_config(page_title="Sustainability Chatbot", layout="wide")
st.title("🌿 Sustainability Report Chatbot (Gemini Free API)")
st.write("Upload a Sustainability Report (PDF) and ask questions based on its content.")

# File uploader
uploaded_file = st.file_uploader("📄 Upload a Sustainability Report PDF", type=["pdf"])

if uploaded_file:
    # Extract text from PDF
    reader = PdfReader(uploaded_file)
    raw_text = ""
    for page in reader.pages:
        content = page.extract_text()
        if content:
            raw_text += content

    # Split text into chunks
    def split_text(text, max_length=500):
        sentences = text.split('. ')
        chunks, chunk = [], ""
        for sentence in sentences:
            if len(chunk) + len(sentence) <= max_length:
                chunk += sentence + ". "
            else:
                chunks.append(chunk.strip())
                chunk = sentence + ". "
        chunks.append(chunk.strip())
        return chunks

    text_chunks = split_text(raw_text)
    chunk_embeddings = embed_model.encode(text_chunks)

    # Store embeddings in FAISS index
    dim = chunk_embeddings[0].shape[0]
    index = faiss.IndexFlatL2(dim)
    index.add(chunk_embeddings)

    # Question input
    query = st.text_input("🔍 Ask a question about the report:")
    if query:
        query_embedding = embed_model.encode([query])
        _, I = index.search(query_embedding, k=3)
        retrieved_chunks = [text_chunks[i] for i in I[0]]

        context = "\n\n".join(retrieved_chunks)
        prompt = f"""You are a helpful assistant. Use the context below to answer the question.

Context:
{context}

Question: {query}
Answer:"""

        # Call Gemini model
        model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")
        with st.spinner("🤖 Generating answer..."):
            response = model.generate_content(prompt)

        st.markdown("### ✅ Gemini's Answer")
        st.write(response.text)
else:
    st.info("Please upload a Sustainability PDF Report to begin.")
