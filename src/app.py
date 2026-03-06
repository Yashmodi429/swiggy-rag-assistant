from vector_store import create_vector_db
from rag_pipeline import load_rag_pipeline


def main():

    print("\nSwiggy Annual Report RAG System\n")

    print("Building vector database...\n")

    # create_vector_db()

    qa_system = load_rag_pipeline()

    print("System ready. Ask questions about Swiggy.\n")

    while True:

        query = input("Enter your question (type exit to quit): ")

        if query.lower() == "exit":
            print("Exiting system.")
            break

        result = qa_system.invoke(query)

        print("\nAnswer:\n")

        print(result["result"])

        print("\nSupporting Context:\n")

        for doc in result["source_documents"]:
            print(doc.page_content[:300])
            print("\n------------------\n")


if __name__ == "__main__":
    main()