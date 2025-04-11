import os
from dotenv import load_dotenv
load_dotenv()
from langchain.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory



embedding = OpenAIEmbeddings(model="text-embedding-3-small")
llm = ChatOpenAI(model="gpt-4o", temperature=0)

allowed_topics = [
    "asthma", "eczema", "atopic eczema", "back pain", "migraine", "type 2 diabetes"
]

blocked_keywords = [
    "copd", "hiv", "insulin resistance", "garlic", "cancer", "depression", "vitamin", "thyroid", "weight loss"
]

vectorstore_path = "vectorstore"
if os.path.exists(vectorstore_path):
    vectorstore = FAISS.load_local(
        folder_path=vectorstore_path,
        embeddings=embedding,
        allow_dangerous_deserialization=True
    )
else:
    vectorstore = None

memory = ConversationBufferMemory(
    memory_key="chat_history",
    output_key="answer",
    return_messages=True
)

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
    memory=memory,
    return_source_documents=True,
    output_key="answer"
)

def ask_question(question):
    q_lower = question.lower()

    if not any(t in q_lower for t in allowed_topics) or any(b in q_lower for b in blocked_keywords):
        return (
            "❌ I'm sorry, but your question seems to be outside the scope of this prototype.\n\n"
            "📚 *This assistant is trained only on the following NHS topics:* " +
            ", ".join([f"*{topic.title()}*" for topic in allowed_topics]) +
            ".\n💡 Please ask something specifically related to those topics.\n\n"
            "⚠️ *This is a prototype and does not provide general medical advice.*",
            []
        )

    result = qa_chain.invoke({"question": question})
    answer = result['answer']
    sources = result['source_documents']

    context_message = (
        "\n\n📚 *This assistant is a prototype trained only on the following NHS documents:* " +
        ", ".join([f"*{topic.title()}*" for topic in allowed_topics]) +
        ".\n💡 It can only answer questions related to these topics."
    )
    disclaimer = "\n\n⚠️ *This is not medical advice. Always consult a healthcare professional.*"

    return answer + context_message + disclaimer, sources
