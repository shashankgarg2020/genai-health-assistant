from src.loader import load_and_split_pdfs
from src.embedder import get_embedder
from langchain.vectorstores import FAISS

# 1. Load and split the NHS PDFs
docs = load_and_split_pdfs("data")

# 2. Load the OpenAI embedder
embedder = get_embedder()

# 3. Create the FAISS vectorstore
vectorstore = FAISS.from_documents(docs, embedder)

# 4. Save vectorstore to disk
vectorstore.save_local("vectorstore")

print("✅ Vectorstore created and saved successfully.")
