from fastapi import FastAPI
from pydantic import BaseModel
import requests
import secret

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

@app.get("/")
def status():
    return {"status":"up"}

@app.post("/push_task", status_code=201)
def post_message(task: Task):

    task_param = task.dict()
    chat_id = task_param.chat_id
    message = task_param.key

    url = f"https://api.telegram.org/bot{secret.TOKEN}/sendMessage?chat_id={chat_id}&text={message}"

    result = requests.get(url)


    return {"result":"1"}