import os
import chromadb

from dotenv import load_dotenv
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# =========================================================
# LOAD ENV
# =========================================================
load_dotenv()

# =========================================================
# CHROMADB CLIENT
# =========================================================
client = chromadb.PersistentClient(
    path="./chroma_db"
)

embedding_func = SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# =========================================================
# CREATE COLLECTION
# =========================================================
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

# =========================================================
# LOAD DOCUMENTS
# =========================================================
loader = DirectoryLoader(
    "./company_docs1",
    glob="**/*.txt",
    loader_cls=TextLoader
)

documents = loader.load()

print(f"Loaded {len(documents)} documents")

# =========================================================
# SPLIT DOCUMENTS
# =========================================================
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks")

# =========================================================
# STORE IN CHROMADB
# =========================================================
for i, chunk in enumerate(chunks):

    collection.add(
        documents=[chunk.page_content],
        ids=[f"doc_{i}"]
    )

print("Documents successfully indexed!")
print("Total documents:", collection.count())
