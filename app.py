import os
import streamlit as st
import chromadb
import requests
from dotenv import load_dotenv
from chromadb.api.types import EmbeddingFunction

load_dotenv()

# =========================================================
# GEMINI EMBEDDINGS (via API call)
# =========================================================
class GeminiEmbeddingFunction(EmbeddingFunction):
    def __init__(self, api_key, model="models/text-embedding-004"):
        self.api_key = api_key
        self.model = model

    def __call__(self, input):
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:embedContent?key={self.api_key}"

        embeddings = []

        for text in input:
            response = requests.post(
                url,
                json={"content": {"parts": [{"text": text}]}},
            )

            if response.status_code != 200:
                raise ValueError(response.text)

            data = response.json()
            embeddings.append(data["embedding"]["values"])

        return embeddings


# =========================================================
# CHROMADB INIT
# =========================================================
@st.cache_resource
def init_chromadb():
    client = chromadb.Client()  # safe for Streamlit Cloud

    embedding_fn = GeminiEmbeddingFunction(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    return client.get_or_create_collection(
        name="company_docs",
        embedding_function=embedding_fn
    )


collection = init_chromadb()


# =========================================================
# GEMINI CHAT RESPONSE
# =========================================================
def gemini_generate(prompt, context):
    api_key = os.getenv("GEMINI_API_KEY")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"""
You are an HR assistant.
Use ONLY the context below.

Context:
{context}

Question:
{prompt}
"""
                    }
                ]
            }
        ]
    }

    response = requests.post(url, json=payload)

    if response.status_code != 200:
        return f"Error: {response.text}"

    data = response.json()

    return data["candidates"][0]["content"]["parts"][0]["text"]


# =========================================================
# RAG FUNCTION
# =========================================================
def get_rag_response(query, n_results=3):
    results = collection.query(query_texts=[query], n_results=n_results)

    docs = results.get("documents", [[]])[0]

    if not docs:
        return "❌ No relevant information found."

    context = "\n\n---\n\n".join(docs)

    return gemini_generate(query, context)


# =========================================================
# STREAMLIT UI
# =========================================================
st.set_page_config(page_title="Company Knowledge Assistant")

st.title("📘 Company Knowledge Assistant (Gemini + RAG)")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Ask something...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_rag_response(prompt)

        st.write(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
