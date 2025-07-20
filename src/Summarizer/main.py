import os
import traceback
from src.Summarizer.logger import logging
from src.Summarizer.utils import read_file
from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate,  HumanMessagePromptTemplate

llm = ChatOllama(model="llama3.1:8b")

TEMPLATE='''
You are the best text summarizer in the world.
Given the following text, summarize it in a clear, concise, and well-structured manner by following the format below.

Output format:
- A summary title: “Summary of [Title] as heading of content”
- The main content:
    - Use clear headings for each key concept
    - List the key points under each heading as bullet points

Guidelines:
- Focus on the most important ideas
- Avoid unnecessary details or repetition
- Use simple, professional language

TEXT: {text}

'''

summarizer_prompt= ChatPromptTemplate.from_messages([
    HumanMessagePromptTemplate.from_template(TEMPLATE)
])

summarizer_chain = summarizer_prompt | llm
