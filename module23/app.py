import streamlit as st
import requests
import pandas as pd

st.title("Project Managment")

st.header("Add Developer")
dev_name = st.text_input("Developer Name")
dev_experience = st.number_input("Experience Years:" , min_value=0, max_value=50 ,value=0)

if st.button("Create developer"):
    dev_data = {"name": dev_name , "experience": dev_experience}
    response = requests.post("http://127.0.0.1:8000/developer/" ,json=dev_data)

st.header("Add a project")
proj_title = st.text_input("Project Title")
proj_desc = st.text_area("Project Desc")
projc_langs = st.text_input("Languages Used")
lead_dev_name = st.text_input("Lead Developer name")
lead_dev_exp = st.number_input("lead dev exp years:", max_value=50 , min_value=0, value=0)

if st.button("Create project"):
    lead_dev_data = {"name": lead_dev_name , "experience": lead_dev_exp}
    proj_data = {
        "title": proj_title,
        "description": proj_desc,
        "languages": projc_langs,
        "lead_developer": lead_dev_data
    }
    response = requests.post("http://127.0.0.1:8000/developer/", json=proj_data)
    st.json(response.json())