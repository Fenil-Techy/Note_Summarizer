from setuptools import setup, find_packages

setup(
    name='Note_Summarizer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'langchain',
        'streamlit',
        'PyPDF2',
        'langchain_ollama',
        'langchain_community'  # or langchain_ollama in your case
    ]
)