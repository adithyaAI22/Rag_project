This project is a full-stack Document Processing and Retrieval-Augmented Generation (RAG) system built using FastAPI, PaddleOCR, LangChain, and Hugging Face models.
It extracts text from scanned documents containing handwritten English and Malayalam text as well as visual elements, using OCR and language models, 
then embeds the content with all-MiniLM-L6-v2 and stores it in a FAISS vector store. A Streamlit frontend allows users to upload documents and ask questions,
which are answered using retrieved context combined with a language model. 
The system is fully containerized using Docker for easy deployment.
