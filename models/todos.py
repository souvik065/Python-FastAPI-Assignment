from pydantic import BasicModel


class Todo(BasicModel):
    name: str
    description: str
    complete:bool
    