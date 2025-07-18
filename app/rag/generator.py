from transformers import pipeline

rag_pipeline = pipeline("text2text-generation", model="google/flan-t5-base", device=-1)

def answer_question(question, context):
    prompt = f"Context: {context}\n\nQuestion: {question}"
    return rag_pipeline(prompt, max_length=200)[0]['generated_text']
