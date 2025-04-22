# 🩺 GenAI Healthcare Assistant (NHS Q&A System)

A production-ready, Retrieval-Augmented Generation (RAG) based AI assistant that accurately answers health-related questions using official NHS clinical documents. This system is built for **high accuracy, low hallucination**, and scalability as documents grow from a few PDFs to thousands.



---

## 🚀 Features

- ✅ **Semantic Document Indexing**: NHS PDFs are semantically chunked and embedded using state-of-the-art models.
- ✅ **Hybrid Retrieval**: Combines vector similarity search (FAISS) with keyword + metadata filtering.
- ✅ **Context-Grounded Answering**: LLMs respond only using retrieved context to avoid hallucinations.
- ✅ **Prompt Guardrails**: Custom system prompts constrain responses to improve clinical reliability.
- ✅ **Scalable Design**: Built to support 1,000+ documents with performance in mind.
- ✅ **Modular Codebase**: Each component (embedding, retrieval, generation) is modular and easy to extend.

---

## 🧠 Architecture Overview

```mermaid
graph TD
    A[User Question] --> B[Hybrid Retriever (FAISS + Filters)]
    B --> C[Relevant Document Chunks]
    C --> D[LLM Generator]
    D --> E[Final Answer (Context-Grounded)]
