import streamlit as st
import requests

st.title("Add a new book App")

userinput = st.sidebar.selectbox("Please check one of the boxes true= Get ",["GetBook"])

if userinput == "GetBook":
    id = st.number_input("books_id")
    if id:
        response = requests.get(
            f"http://127.0.0.1:8000/books_id={id}"
        )
        if response.status_code == 200:
            id = st.number_input("books_id")
            st.write("title", response.json()("books"))
            st.write("author", response.json()("books"))