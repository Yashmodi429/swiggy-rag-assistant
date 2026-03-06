Swiggy Annual Report AI Assistant (RAG Chatbot)

An AI-powered chatbot that answers questions from the Swiggy Annual Report using Retrieval-Augmented Generation (RAG).

The system retrieves relevant information from the report and generates accurate answers using a local LLM.

🚀 Features

📄 Ask questions about Swiggy's annual report

🔍 Semantic search using FAISS vector database

🤖 AI responses powered by a local LLM (Ollama)

💬 ChatGPT-style interactive UI with Streamlit

📚 Shows supporting context from the report

⚡ Fast and efficient RAG pipeline

🧠 Tech Stack

Python

LangChain

FAISS (Vector Database)

Sentence Transformers (Embeddings)

Ollama (Local LLM)

Streamlit (Frontend UI)

📂 Project Structure
swiggy-rag-assistant
│
├── data
│   └── swiggy_report.pdf
│
├── src
│   ├── ingest.py
│   ├── vector_store.py
│   ├── rag_pipeline.py
│   ├── ui.py
│   └── app.py
│
├── requirements.txt
├── README.md
└── .gitignore
⚙️ Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/swiggy-rag-assistant.git
cd swiggy-rag-assistant

Install dependencies:

pip install -r requirements.txt
🤖 Install Local LLM

Install Ollama:

https://ollama.com/download

Pull the model:

ollama pull phi3
📊 Create Vector Database

Run:

python src/vector_store.py

This will:

Load the PDF

Split the document

Generate embeddings

Create FAISS vector index

💬 Run the Chatbot

Start the UI:

streamlit run src/ui.py

Open browser:

http://localhost:8501
🧪 Example Questions

Try asking:

What is Swiggy Instamart?

How many restaurant partners does Swiggy have?

In how many cities does Swiggy operate?

What was Swiggy's net loss after tax in FY2024?

Who is the Chief Financial Officer of Swiggy?

📸 Demo

Example UI:

User: What is Swiggy Instamart?

AI:
Swiggy Instamart is a quick commerce service offering
grocery delivery in minutes through a network of dark stores.
📈 How RAG Works

The PDF is split into chunks

Each chunk is converted into vector embeddings

Stored inside a FAISS vector database

When a question is asked:

Relevant chunks are retrieved

Context is sent to the LLM

The LLM generates an answer using that context

🔒 Security

API keys and environment files are excluded using .gitignore.

👨‍💻 Author

Yash Modi

GitHub:
https://github.com/Yashmodi429

⭐ Future Improvements

PDF page highlighting

Streaming responses

Chat memory

Multi-document support

Deployment on cloud
