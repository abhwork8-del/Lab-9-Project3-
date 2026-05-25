# Project3
# Lab 9 — 10
# Generative AI Domain Assistant & Retrieval-Augmented Generation (RAG) Pipeline
This project showcases the complete implementation of a conversational AI system integrated with a localized document lookup mechanism. Spanning across two technical milestones, the system demonstrates how a baseline Large Language Model (LLM) can be adapted from a generic chat interface into highly restricted, domain-specific enterprise agents using the Google GenAI SDK and Gemini architecture.
# System Objectives & Milestones
# Lab 9: GenAI Domain Assistant
The primary objective of this phase was to establish safe API client initialization and implement foundational conversational structures. 
Stateful Dialogue History: Configured a multi-turn chat framework that dynamically records back-and-forth messaging history so the engine retains conversational context over time.
Behavioral Prompt Engineering: Utilized system instructions to isolate the AI's persona, setting rules, tone constraints, and factual scopes to build two distinct operational variants:
1. HR Policy Assistant: Tailored to respond strictly to employee inquiries regarding vacation accrual rules, parental leave, and remote workspace allowances.
2. Customer Support Agent: Optimized with an empathetic, solution-oriented tone designed to handle warranty parameters, return windows, and multi-tier escalation criteria.
# Lab 10: Retrieval-Augmented Generation (RAG)
The objective of this phase was to mitigate model hallucinations and eliminate reliance on public training data by forcing the AI to verify queries against a customized internal text database.
Data Ingestion & Text Fragmentation: Established pipeline operations to ingest unstructured text data from corporate policy files. These files were programmatically broken down into uniform character tracking windows with intentional segment overlapping to prevent context severing.
Algorithmic Document Retrieval: Coded a modular frequency-matching search engine to parse data fragments, automatically scoring and ranking the most contextually relevant entries relative to incoming user queries.
Context-Grounded Inference Pipeline: Tied the search engine's outputs directly into the generation layer. When a user asks a question, the top matching documentation blocks are woven directly into a specialized context template alongside the question.
Rigid Error Fallback Rules: Engineered strict boundaries ensuring that if a query references parameters outside the provided data assets (such as missing corporate health insurance criteria), the system rejects standard creative guessing and cleanly surfaces a standardized missing-context warning.
# System File Architecture
The underlying structure of the deployment environment handles raw enterprise data storage alongside processing runtimes as outlined below:
1. company_docs: The localized corporate data layer repository.
2. hr_policy.txt: Contains official parameters for full-time employee vacations, remote working, and parental care leaves.
3. it_policy.txt: Defines parameters for company-issued hardware security protocols, VPN prerequisites, and workplace dress codes.
labs_9_and_10_gemini.ipynb: The complete combined execution notebook containing environment setups, credential management, multi-turn chat loops, and the completed grounding pipeline.
# Evaluation Summary: Standard Inference vs. RAG Execution
The final stage of development validated the system by executing identical queries through an ungrounded model versus the completed RAG pipeline to contrast behaviors:
1. Standard Inference (Without RAG): When asked specific corporate policy questions, the standard model relies on its generalized public training data. This leads to broad industry estimates, generic averages, or outright guesswork regarding company rules.
2. Grounded Inference (With RAG): When the same query passes through the RAG pipeline, the model is restricted to a zero-ingestion parameters profile. It completely ignores public web assumptions and extracts the precise, mathematically definitive parameters written directly in your documentation files.

# Lab 11 – Vector Databases & Semantic Search (Gemini API)
# Overview
This project implements **Lab 11: Vector Databases & Semantic Search**.
The objective of this lab is to upgrade traditional keyword search into **semantic search** using **embeddings** and a **vector database (ChromaDB)**.
Unlike exact keyword matching, semantic retrieval understands the meaning of text and returns relevant information even when different words are used.
This implementation uses **Google Gemini API** instead of OpenAI for embedding generation and response generation.
# Objectives
By completing this lab, the following concepts were implemented:
1. Generate embeddings using Gemini API
2. Calculate cosine similarity between vectors
3. Store embeddings inside ChromaDB
4. Build semantic document retrieval
5. Implement Retrieval-Augmented Generation (RAG)
6. Compare semantic search with traditional keyword search
# Technologies Used
1. Python
2. Google Gemini API
3. ChromaDB
4. LangChain
5. NumPy
6. Kaggle Notebook
# Project Structure
plaintext
Lab11_Vector_DB/
company_docs:
1. vacation_policy.txt
2. remote_work.txt
3. maternity_leave.txt
chroma_db: 
1. week11_semantic_search.ipynb
2. README.md
3. requirements.txt
# Installation
Install dependencies:
pip install google-generativeai
pip install chromadb
pip install langchain
pip install langchain-community
pip install langchain-text-splitters
pip install sentence-transformers
pip install numpy
# API Configuration
Create a Gemini API key.
# Workflow
# 1. Generate Embeddings
Text is converted into numerical vectors using Gemini embedding models.
# 2. Similarity Calculation
Cosine similarity measures semantic closeness.
# 3. Create Chroma Vector Database
Documents are stored together with embeddings.
# 4. Perform Semantic Search
Semantic search retrieves meaning rather than exact words.
# 5. Build Semantic RAG
Pipeline:
User Question
↓
Generate Embedding
↓
Vector Search
↓
Retrieve Context
↓
Gemini Generates Answer
# Example Questions
Example inputs:
How much vacation leave?
Can employees work remotely?
What is maternity leave policy?
outputs:
20 vacation days
3 work-from-home days
90 maternity leave days
# Results
Successfully implemented:
1. Embedding generation
2. Similarity computation
3. ChromaDB indexing
4. Vector retrieval
5. Semantic RAG pipeline
6. Question answering using retrieved context
# Learning Outcomes
This lab demonstrates:
1. Understanding embeddings
2. Semantic understanding of text
3. Vector databases
4. Retrieval-Augmented Generation
5. Production-style search pipelines

## Author
Aliha Batool
Lab 11 – Week 11

# Week 12: Streamlit Deployment + Interactive AI Assistant
# Streamlit Web Application
Developed a full interactive web app using Streamlit.
Features:
1. Chat interface
2. Real-time AI responses
3. Sidebar controls
4. Conversation history
5. Interactive UI components
# Session State Management
Implemented:
1. Persistent conversation memory
2. Chat history tracking
3. Dynamic UI updates
4. Stateful interactions

# Interactive RAG Assistant
Users can:
1. Ask document-related questions
2. Retrieve grounded answers
3. Interact with AI in real time
4. Query indexed company knowledge

# Cached Resource Optimization
Optimized performance using:
1. @st.cache_resource
2. Cached model loading
3. Cached ChromaDB initialization
4. Reduced API overhead

# Error Handling & Stability
Improved robustness with:
1. Global exception handling
2. User-friendly error messages
3. Missing database detection
4. API failure recovery

# Technology
1. Python 3.x
2. Google Gemini API
3. Streamlit
4. ChromaDB
5. LangChain
6. LangChain Google GenAI
7. SentenceTransformers
8. python-dotenv
9. Jupyter Notebook
10. Kaggle
11. VS Code

# Models Used
# LLMs
gemini-pro
gemini-1.5-pro
gemini-1.5-flash
# Embedding Models
all-MiniLM-L6-v2
# Key Concepts Covered
1. Prompt Engineering
2. Multi-turn Conversations
3. Domain-Specific AI Assistants
4. Retrieval-Augmented Generation (RAG)
5. Semantic Search
6. Vector Databases
7. ChromaDB
8. Embeddings
9. LangChain Pipelines
10. Streamlit Deployment
11. Context Injection
12. Document Chunking
13. Persistent Memory
14. API Integration
15. Error Handling
16. Hallucination Reduction
17. Semantic Retrieval
18. Conversational AI Systems
# Example Capabilities
# HR Assistant
"How many vacation days do employees get?"
# Customer Support Assistant
"Can I return a laptop after 15 days?"
# RAG-Based QA
Answers questions strictly from uploaded documents.
If information is unavailable:
"Not found in documents"
# Deliverables Completed
 1. Documents loaded from directory
 2. Text preprocessing pipeline implemented
 3. Recursive text chunking completed
 4. Chunk preview generation
 5. Semantic embedding pipeline created
 6. ChromaDB vector database integrated
 7. Persistent vector storage implemented
 8. Retrieval system implemented
 9. Semantic similarity search added
 10. Tested retrieval queries
 11. RAG query pipeline implemented
 12. Gemini-powered grounded responses generated
 13. Hallucination prevention implemented
 14. RAG vs non-RAG comparison completed
 15. Streamlit web application developed
 16. Interactive chatbot interface created
 17. Session-state conversation memory implemented
 18. Sidebar analytics added
 19. Cached resource optimization completed
 20. Gemini API integration completed
 21. LangChain integration completed
 22. Error handling implemented
 23. End-to-end conversational RAG assistant deployed

# About 
Aliha Batool — Project 3
