import os
import traceback
from langchain_ollama import ChatOllama
from src.Summarizer.main import summarizer_chain
from src.Summarizer.utils import read_file
from fpdf import FPDF

import streamlit as st

st.set_page_config(page_title="Note Summarizer", page_icon=":book:", layout="wide")
st.title("Note Summarizer")

uploaded_file = st.file_uploader("Upload a PDF or text file", type=["pdf", "txt"])

button= st.button("Summarize")

if button:
    with st.spinner("Processing..."):
        if uploaded_file is not None:
            text = read_file(uploaded_file)
            try:
                response= summarizer_chain.invoke({"text": text})
                summary = response.content
                st.write(summary)
                clean_summary = summary.replace("•", "-").replace("**", " ")
                pdf = FPDF()
                pdf.set_font("Arial", size=12)

                pdf.add_page()
                for line in clean_summary.splitlines():
                    pdf.multi_cell(0, 8, line)

                pdf.output("summary.pdf")

                with open("summary.pdf", "rb") as f:
                    st.download_button(
                        label="📄 Download Summary as PDF",
                        data=f,
                        file_name="summary.pdf",
                        mime="application/pdf"
                    )
            except Exception as e:
                st.error(f"Error during summarization: {e}")
        else:
            st.error("Failed to read the file. Please upload a valid PDF or text file.")

