import streamlit as st
import requests

st.title("📄 Document Chat (English & Malayalam Handwriting + Charts)")

with st.sidebar:
    st.header("Upload Scanned Image")
    uploaded_file = st.file_uploader("Choose image", type=["png", "jpg", "jpeg"])

    if uploaded_file:
        with open(f"data/uploads/{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("Uploaded!")
        res = requests.post("http://localhost:8000/upload/", files={"file": open(f"data/uploads/{uploaded_file.name}", "rb")})
        ##st.write(res.json())

        st.write("Response Status:", res.status_code)
        st.write("Raw Response Text:", res.text)  # Debug this


st.header("Ask Your Question")
query = st.text_input("Type your question here:")

if st.button("Ask") and query:
    res = requests.post("http://localhost:8000/ask/", json={"query": query})
    st.markdown(f"**Answer:** {res.json()['answer']}")
