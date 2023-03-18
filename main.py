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
    chat_id = task_param['chat_id']
    key = task_param['key']
    sum = task_param['sum']
    priority = task_param['priority']
    type = task_param['type']
    status = task_param['status']
    created = task_param['created']

    alert = f"Новый {type} c {priority} приоритетом!!!\n\nhttps://jira.app.local/browse/{key}\n\n{sum}\n\n{created}"

    url = f"https://api.telegram.org/bot{secret.TOKEN}/sendMessage?chat_id={chat_id}&text={message}"

    result = requests.get(url)


    return {"result":"1"}