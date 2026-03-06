from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from ingest import load_documents


def create_vector_db():

    docs = load_documents()

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(docs, embeddings)

    db.save_local("faiss_index")

    print("Vector database created successfully!")


if __name__ == "__main__":
    create_vector_db()