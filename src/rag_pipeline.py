from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM


def load_rag_pipeline():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k":5}
    )

    llm = OllamaLLM(model="phi3")

    def ask(question):

        docs = retriever.invoke(question)

        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
You are an AI assistant answering questions using the Swiggy Annual Report.

IMPORTANT RULES:
1. Answer ONLY using the context.
2. If answer is not present say:
"I could not find this in the Swiggy Annual Report."
3. Give short factual answers.

Context:
{context}

Question:
{question}

Answer:
"""

        answer = llm.invoke(prompt)

        return {
            "result": answer,
            "source_documents": docs
        }

    return ask