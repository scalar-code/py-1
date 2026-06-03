from fastapi import FastAPI
import database
# import pydanticnames
from pydanticnames import Name, NamesCreate
app = FastAPI()


@app.post("/name/")
def create_item(name: NamesCreate):
    name = database.create_name(name)
    return name.create_name()
@app.get("/name/{name_id}")
def read_item(name_id: int, name:str):
    name = database.read_name(name_id)
    return name.read_name()
@app.delete("/name/{name_id}")
def delete_item(name_id = int):
    name = database.delete_name(name_id)
    return name.delete_name()