# AI-MediCare

# **FOR EDUCATIONAL PURPOSES ONLY**

# MediBot - AI Medical Assistant

## Overview
MediBot is an AI-powered chatbot designed to assist users by providing preliminary medical-related advice based on their queries. It leverages advanced NLP models to analyze user input, retrieve relevant medical data, and generate responses. MediBot is not a replacement for professional medical consultation but serves as an informational assistant.

## Features
- Utilizes **Google Gemini AI** for embeddings and chatbot responses.
- **ChromaDB** for efficient similarity search and retrieval.
- **Streamlit** for an interactive and user-friendly web interface.
- **LangChain** for document processing and question-answering.
- Supports PDF-based medical knowledge extraction.

## Technologies Used
- **LLM Model:** Google Generative AI (Gemini API)
- **Vector Database:** ChromaDB
- **Frameworks & Libraries:** LangChain, Streamlit, PyMuPDF
- **Development Tools:** Python, VS Code

## Data Source
- The chatbot processes and retrieves medical information from uploaded PDFs using **PyMuPDF**.
- The extracted content is stored and indexed using **ChromaDB** for quick retrieval.

## Usage
1. Users enter a medical query, age, disease type, and symptoms.
2. The chatbot retrieves relevant medical information using similarity search.
3. A response is generated based on the retrieved data and user input.

## ⚠️ Disclaimer
- **MediBot is for educational purposes only.** It is not a substitute for professional medical advice, diagnosis, or treatment.
- Always consult a qualified healthcare provider for medical concerns.
- The chatbot's responses are based on available data and may not be exhaustive or entirely accurate.

## Limitations
- **MediBot does not provide medical diagnoses.** Users should consult a healthcare professional for medical concerns.
- Limited to the information available in the uploaded documents.

## Future Enhancements
- Expand the database with additional medical resources.
- Improve the chatbot’s NLP capabilities for more accurate responses.
- Introduce voice-based interactions for accessibility.

## License
This project is licensed under the MIT License.

