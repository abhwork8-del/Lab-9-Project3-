import os
import streamlit as st
import chromadb
from google import genai
from dotenv import load_dotenv

# ==========================================
# TASK 3.3: TOP-LEVEL ERROR HANDLING
# ==========================================
try:
    # Load environment variables
    load_dotenv()

    # Page Configuration
    st.set_page_config(
        page_title="AI HR Knowledge Assistant",
        page_icon="🤖",
        layout="wide"
    )

    # ==========================================
    # TASK 2.2: INITIALIZE RESOURCE CACHING
    # ==========================================
    @st.cache_resource
    def init_chromadb():
        """Initializes and caches the persistent ChromaDB client."""
        if not os.path.exists("./chroma_db"):
            raise FileNotFoundError("ChromaDB directory not found.")
        
        # Initialize client referencing local persistent storage
        client = chromadb.PersistentClient(path="./chroma_db")
        
        # Retrieve the existing collection built during Week 11
        collection = client.get_collection(name="company_docs")
        return collection

    @st.cache_resource
    def init_gemini():
        """Initializes and caches the Gemini API Client."""
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            st.warning("GEMINI_API_KEY is missing from environment variables or secrets.")
        return genai.Client(api_key=api_key)

    # Initialize connections
    collection = init_chromadb()
    client = init_gemini()

    # ==========================================
    # TASK 2.3: REFINED GEMINI RAG FUNCTION
    # ==========================================
    def get_rag_response(query, n_results=3):
        """Queries ChromaDB and generates context-aware answers via Gemini API."""
        try:
            # Query vector database using raw text
            results = collection.query(
                query_texts=[query],
                n_results=n_results
            )
            
            # Check if matching context exists
            if not results or not results['documents'] or len(results['documents'][0]) == 0:
                return "No relevant information found in corporate knowledge base documents."
            
            # Formulate structural context string
            context = "\n\n---\n\n".join(results['documents'][0])
            
            # System instructions and prompt construction
            prompt = f"""You are a helpful HR assistant. Answer using ONLY the context below. 
If the information is not explicitly mentioned in the context, state that you do not know. 
Be concise, accurate, professional, and friendly.

Context:
{context}

Question: {query}
Answer:"""

            # Call Gemini API using standard text generation model
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            return response.text

        except Exception as e:
            return f"Error executing model pipeline: {str(e)}"

    # ==========================================
    # TASK 3.1: SIDEBAR INTERFACE & STATS
    # ==========================================
    with st.sidebar:
        st.header("About")
        st.markdown("""
        This AI assistant can seamlessly answer questions regarding:
        * 🏠 Remote work guidelines
        * 👶 Parental leave
        * 🌴 Vacation policies
        * 🏥 Benefits information
        """)
        
        st.divider()
        st.subheader("Powered By")
        st.caption("⚡ Gemini 2.5 Flash")
        st.caption("📂 ChromaDB Vector Search")
        
        st.divider()
        st.subheader("System Metrics")
        # Display dynamic metrics using database counts and conversation length
        st.metric("Indexed Documents", collection.count())
        st.metric("Active Session Messages", len(st.session_state.get('messages', [])))
        
        st.divider()
        # Clear Chat History UI Routine
        if st.button("Clear Chat History", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

    # ==========================================
    # MAIN INTERFACE IMPLEMENTATION
    # ==========================================
    st.title("🏢 Company Knowledge Assistant")
    st.markdown("Ask me anything about company internal policies, benefits, or workflows!")

    # Setup Session State for Chat History Tracking
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # TASK 3.2: ASSISTANT WELCOME MESSAGE
    if len(st.session_state.messages) == 0:
        welcome_msg = """Hi! I'm your company knowledge assistant. I can help you find information about:
* Remote work guidelines
* Vacation and time off policies
* Parental leave benefits
* And more!

Just ask a question below to get started."""
        with st.chat_message("assistant"):
            st.write(welcome_msg)

    # Render ongoing conversational timeline logs
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Handle Active Live User Input Pipelines
    if prompt := st.chat_input("Ask a question regarding company workflows..."):
        # Log User Entry
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
            
        # Call RAG Pipeline with Loading Spinner State UI
        with st.chat_message("assistant"):
            with st.spinner("Searching matching knowledge documents..."):
                response = get_rag_response(prompt)
                st.write(response)
                
        # Append response to memory log tracking array
        st.session_state.messages.append({"role": "assistant", "content": response})

except FileNotFoundError as e:
    st.error(f"❌ Initialization Error: {str(e)}")
    st.info("Please verify your 'chroma_db' data folder is copied inside the 'project_3_app' directory.")
    st.stop()
except Exception as e:
    st.error(f"❌ Fatal Application Exception: {str(e)}")
    st.stop()
