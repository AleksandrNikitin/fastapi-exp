from fastapi import FastAPI
from pydantic import BaseModel
import requests
import secret
from emoji import emojize


class Task(BaseModel):
    chat_id: str
    key: str
    sum: str
    priority: str
    type: str
    created: str

class Alert(BaseModel):
    chat_id: str
    task_key: str
    task_sum: str
    message: str

app = FastAPI()

@app.get("/")
async def get_status():
    return {"status":"up"}


@app.post("/push_task", status_code=201)
async def push_task(task: Task):
    task_param = task.dict()

    if task_param['type'] == 'Письмо':
        title = 'Внимание! Новое Письмо!'
    else:
        title = f"Внимание! Новый {task_param['type']}!"

    message = f"{emojize(':red_circle:', language='alias')}{title}\n" \
              f"{emojize(':bangbang:', language='alias')}{task_param['priority']} приоритет\n\n" \
              f"https://jira.app.local/browse/{task_param['key']}\n\n" \
              f"{task_param['sum']}\n\n" \
              f"Дата создания: {task_param['created']}"

    url = f"https://api.telegram.org/bot{secret.TOKEN}/sendMessage?chat_id={task_param['chat_id']}&text={message}"
    result = requests.get(url)
    return {"result":"1"}


@app.post("/push_alert", status_code=201)
async def push_alert(alert: Alert):
    alert_param = alert.dict()

    message = f"{emojize(':red_circle:', language='alias')}Внимание!\n"\
              f"{emojize(':alarm_clock:', language='alias')}{alert_param['message']}\n\n" \
              f"https://jira.app.local/browse/{alert_param['task_key']}\n" \
              f"{alert_param['task_sum']}\n" \


    url = f"https://api.telegram.org/bot{secret.TOKEN}/sendMessage?chat_id={alert_param['chat_id']}&text={message}"
    result = requests.get(url)
    return {"result":"1"}