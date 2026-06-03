from pydantic import BaseModel


class NamesCreate(BaseModel):
    name: str
    surname: str
class Name(NamesCreate):
    id: int