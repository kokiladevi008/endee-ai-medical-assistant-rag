import streamlit as st
from rag_pipeline import RAGPipeline
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="AI Medical Assistant",
    page_icon="🩺",
    layout="centered"
)

# Title
st.title("🩺 AI Medical Assistant (RAG + Endee + Claude)")
st.write("Ask medical questions based on a curated knowledge base of 12 conditions.")

# Initialize RAG pipeline (cached for performance)
@st.cache_resource
def load_pipeline():
    return RAGPipeline()

rag = load_pipeline()

# Input box
user_query = st.text_input("💬 Enter your medical question:")

# Button
if st.button("Get Answer"):

    if not user_query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Searching medical knowledge base..."):

            result = rag.run(user_query)

            st.subheader("📌 Retrieved Context")
            for i, chunk in enumerate(result["context"], 1):
                st.markdown(f"**{i}.** {chunk}")

            st.subheader("🧠 Final Answer")

            if result.get("answer"):
                st.success(result["answer"])
            else:
                st.info("No LLM key found. Showing only retrieved results.")

# Footer
st.markdown("---")
st.caption("⚠️ Educational use only. Not a substitute for professional medical advice.")
