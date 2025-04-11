from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def load_and_split_pdfs(folder_path):
    all_docs = []
    for file in os.listdir(folder_path):
        if file.endswith('.pdf'):
            loader = PyPDFLoader(os.path.join(folder_path, file))
            all_docs.extend(loader.load())

    print(f"✅ Loaded {len(all_docs)} documents.")

    # Use the same chunking logic as in Colab
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )
    docs = text_splitter.split_documents(all_docs)
    print(f"✅ Split into {len(docs)} chunks.")

    return docs
