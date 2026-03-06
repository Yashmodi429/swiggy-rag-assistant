import streamlit as st
from rag_pipeline import load_rag_pipeline

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Swiggy AI Assistant",
    page_icon="🍔",
    layout="wide"
)

# ---------------- CSS FUTURISTIC STYLE ----------------
st.markdown("""
<style>

/* Main Background */
.stApp{
background: linear-gradient(135deg,#0f172a,#020617);
color:white;
}

/* Title */
.title{
text-align:center;
font-size:42px;
font-weight:700;
color:#FC8019;
margin-top:10px;
}

/* Hero image */
.hero{
border-radius:14px;
margin-bottom:20px;
}

/* Sidebar */
section[data-testid="stSidebar"]{
background:#020617;
}

/* Sidebar header */
.sidebar-title{
color:#FC8019;
font-size:20px;
font-weight:600;
}

/* Chat bubbles */

.user-msg{
background:#FC8019;
color:white;
padding:12px 16px;
border-radius:14px;
margin-bottom:12px;
width:fit-content;
margin-left:auto;
font-size:16px;
box-shadow:0 0 10px rgba(252,128,25,0.6);
}

.bot-msg{
background:rgba(30,41,59,0.7);
backdrop-filter:blur(10px);
color:#e5e7eb;
padding:14px 18px;
border-radius:14px;
margin-bottom:20px;
width:fit-content;
max-width:70%;
font-size:16px;
border:1px solid rgba(255,255,255,0.05);
}

/* Input */
.stChatInput textarea{
border:2px solid #FC8019;
border-radius:10px;
}

/* Source card */
.source{
background:#020617;
border-left:4px solid #FC8019;
padding:10px;
border-radius:8px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO IMAGE ----------------
st.image(
    "https://images.unsplash.com/photo-1504674900247-0877df9cc836",
    use_container_width=True
)

# ---------------- TITLE ----------------
st.markdown(
    '<div class="title">🍔 Swiggy Annual Report AI Assistant</div>',
    unsafe_allow_html=True
)

st.write("Ask questions about the **Swiggy Annual Report 2023-2024**")

# ---------------- LOAD RAG ----------------
@st.cache_resource
def load_system():
    return load_rag_pipeline()

qa_system = load_system()

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "contexts" not in st.session_state:
    st.session_state.contexts = []

# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.markdown('<div class="sidebar-title">💬 Chat History</div>', unsafe_allow_html=True)

    if st.button("🆕 New Chat"):
        st.session_state.messages = []
        st.session_state.contexts = []
        st.rerun()

    for msg in st.session_state.messages:

        if msg["role"] == "user":

            preview = msg["content"][:35]

            st.markdown(
                f"""
                <div style="background:#111827;padding:8px;border-radius:6px;margin-bottom:6px;">
                {preview}...
                </div>
                """,
                unsafe_allow_html=True
            )

# ---------------- CHAT DISPLAY ----------------
for i, msg in enumerate(st.session_state.messages):

    if msg["role"] == "user":

        st.markdown(
            f'<div class="user-msg">{msg["content"]}</div>',
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f'<div class="bot-msg">{msg["content"]}</div>',
            unsafe_allow_html=True
        )

        # Show supporting context
        if i < len(st.session_state.contexts):

            with st.expander("📄 Sources from Annual Report"):

                for j, doc in enumerate(st.session_state.contexts[i]):

                    text = doc.page_content[:500]

                    st.markdown(
                        f'<div class="source"><b>Source {j+1}</b><br>{text}...</div>',
                        unsafe_allow_html=True
                    )

# ---------------- CHAT INPUT ----------------
query = st.chat_input("Ask a question about Swiggy")

# ---------------- ANSWER ----------------
if query:

    st.session_state.messages.append({
        "role":"user",
        "content":query
    })

    with st.spinner("Analyzing Swiggy Annual Report..."):

        result = qa_system(query)

        answer = result["result"]
        docs = result["source_documents"]

    st.session_state.messages.append({
        "role":"assistant",
        "content":answer
    })

    st.session_state.contexts.append(docs)

    st.rerun()