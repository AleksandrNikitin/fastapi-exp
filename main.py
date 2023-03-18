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


@app.post("/push_task")
def post_message(task: Task):
    print(task)
    return task