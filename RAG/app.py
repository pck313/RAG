import streamlit as st

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_openai import ChatOpenAI
from pydantic import SecretStr


emb = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

@st.cache_resource
def load_db():

    loader = PyPDFLoader(
        "data/10trang.pdf"
    )

    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(docs)

    db = FAISS.from_documents(chunks, emb)

    return db

db = load_db()


llm = ChatOpenAI(

    api_key=SecretStr("sk-7v01joFHtMTQaMHtT0usLw"),

    base_url="https://ai.dxhub.com.vn/v1",

    model="Qwen3.6-27B",

    temperature=0
)

st.title("PDF Chatbot - Qwen")

q = st.text_input("Nhập câu hỏi:")

if q:

    docs = db.similarity_search(q, k=3)

    context = "\n\n".join(
        [d.page_content for d in docs]
    )

    prompt = f"""


Context:
{context}

Question:
{q}
"""

    ans = llm.invoke(prompt)

    st.markdown("### Trả lời:")
    st.write(ans.content)