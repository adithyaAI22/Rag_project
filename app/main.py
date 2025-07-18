from fastapi import FastAPI, UploadFile, File
import os

from app.ocr.english import extract_english_text
from app.ocr.malayalam import extract_malayalam_text
from app.rag.embed import get_embeddings
from app.rag.faiss_store import FAISSStore
from app.rag.generator import answer_question

app = FastAPI()
store = FAISSStore()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    path = f"data/uploads/{file.filename}"
    with open(path, "wb") as f:
        f.write(await file.read())

    eng_text = extract_english_text(path)
    mal_text = extract_malayalam_text(path)
    combined = eng_text + "\n" + mal_text
    embeddings = get_embeddings([combined])
    store.add(embeddings, [combined])

    return {"message": "File processed and indexed."}

@app.post("/ask/")
async def ask_question_api(query: str):
    query_embedding = get_embeddings([query])[0]
    context = " ".join(store.search(query_embedding))
    answer = answer_question(query, context)
    return {"answer": answer}
