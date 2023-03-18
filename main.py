from fastapi import FastAPI
from pydantic import BaseModel


# Message class defined in Pydantic
class Task(BaseModel):
    chat_id: str
    key: str
    sum: str
    descr: str
    priority: str
    type: str
    status: str
    created: str

app = FastAPI()


@app.post("/push_task", status_code=201)
def post_message(task: Task):
    return {"result":1}