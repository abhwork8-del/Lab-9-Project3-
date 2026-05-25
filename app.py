import streamlit as st
import os
import chromadb

from dotenv import load_dotenv
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from langchain_google_genai import ChatGoogleGenerativeAI

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Company Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)

# =========================================================
# LOAD ENV VARIABLES
# =========================================================
load_dotenv()

# =========================================================
# CHROMADB INITIALIZATION
# =========================================================
@st.cache_resource
def init_chromadb():

    client = chromadb.PersistentClient(
        path="./chroma_db"
    )

    # Local Embedding Model
    embedding_func = SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )

    # Create collection if not exists
    try:
        collection = client.get_collection(
            name="company_docs1",
            embedding_function=embedding_func
        )

    except:
        collection = client.create_collection(
            name="company_docs1",
            embedding_function=embedding_func
        )

    return collection


# =========================================================
# GEMINI LLM INITIALIZATION
# =========================================================
@st.cache_resource
def init_llm():

    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("Gemini_API_Key"),
        temperature=0
    )

# =========================================================
# INITIALIZE COMPONENTS
# =========================================================
try:

    collection = init_chromadb()
    llm = init_llm()

    # =========================================================
    # TITLE
    # =========================================================
    st.title("🤖 Company Knowledge Assistant")

    st.markdown(
        "Ask me anything about company policies!"
    )

    # =========================================================
    # SESSION STATE
    # =========================================================
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # =========================================================
    # SIDEBAR
    # =========================================================
    with st.sidebar:

        st.header("About")

        st.markdown("""
        This AI assistant can answer questions about:

        - Vacation policies
        - Remote work guidelines
        - Parental leave
        - Benefits information

        Powered by:
        - Google Gemini
        - ChromaDB vector search
        - Semantic RAG
        """)

        st.divider()

        st.metric(
            "Documents Indexed",
            collection.count()
        )

        st.metric(
            "Messages in Chat",
            len(st.session_state.messages)
        )

        st.divider()

        if st.button("Clear Chat History"):

            st.session_state.messages = []

            st.rerun()

    # =========================================================
    # WELCOME MESSAGE
    # =========================================================
    if len(st.session_state.messages) == 0:

        welcome = """
        Hi! I'm your company knowledge assistant.

        I can help you find information about:

        - Vacation and time off policies
        - Remote work guidelines
        - Parental leave benefits
        - And more!

        Just ask me a question to get started.
        """

        with st.chat_message("assistant"):
            st.write(welcome)

    # =========================================================
    # DISPLAY CHAT HISTORY
    # =========================================================
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.write(message["content"])

    # =========================================================
    # RAG FUNCTION
    # =========================================================
    def get_rag_response(query, n_results=3):

        try:

            results = collection.query(
                query_texts=[query],
                n_results=n_results
            )

            if not results["documents"][0]:

                return "No relevant information found."

            context = "\n\n---\n\n".join(
                results["documents"][0]
            )

            prompt = f"""
You are a helpful HR assistant.

Answer using ONLY the context below.

If answer is not found in context,
say you do not know.

Be concise and friendly.

Context:
{context}

Question:
{query}

Answer:
"""

            response = llm.invoke(prompt)

            return response.content

        except Exception as e:

            return f"Error: {str(e)}"

    # =========================================================
    # CHAT INPUT
    # =========================================================
    if prompt := st.chat_input("Ask a question..."):

        # Save User Message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.write(prompt)

        # Assistant Response
        with st.chat_message("assistant"):

            with st.spinner("Searching documents..."):

                response = get_rag_response(prompt)

                st.write(response)

        # Save Assistant Response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

# =========================================================
# GENERAL ERROR
# =========================================================
except Exception as e:

    st.error(f"Error: {str(e)}")

    st.info("""
    Make sure:

    - GEMINI_API_KEY exists in .env
    - chroma_db folder exists
    - company_docs1 collection exists
    """)

    st.stop()
