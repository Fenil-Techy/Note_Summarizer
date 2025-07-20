import os
import traceback
from src.Summarizer.logger import logging
from PyPDF2 import PdfReader

def read_file(uploaded_file):
    if uploaded_file.name.endswith('.pdf'):
        try:
            reader=PdfReader(uploaded_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text.strip()
        except Exception as e:
            logging.error(f"Error reading PDF file: {e}")
            return None
    elif uploaded_file.name.endswith('.txt'):
        try:
            return uploaded_file.read().decode('utf-8').strip()
        except Exception as e:
            logging.error(f"Error reading text file: {e}")
            return None
    else:
        print("Unsupported file format. Please upload a PDF or text file.")
        return None
            