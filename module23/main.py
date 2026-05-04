from altair.theme import names
from fastapi import FastAPI
from models import Developer , Project

app = FastAPI()


@app.post("/developer/")
def create_developer(developer: Developer):
    return {"message" : "Developer Created" , "developer": developer}

@app.post("/project/")
def create_project(project: Project):
    return {"message" : "Project created" , "Project": project}


@app.get("/project/")
def get_projects():
    sample_project = Project(
        title="Test" ,
        description="This is a test project",
        languages=["Python" , "php"],
        lead_developer= Developer(name="Dreni", experience=5)
    )