from fastapi import FastAPI
from pydantic import BaseModel


# Message class defined in Pydantic
class Message(BaseModel):
    channel: str
    author: str
    text: str


app = FastAPI()

@app.get("/show")
async def root():
    return {"message": "Hello World"}

@app.post("/post_message")
def post_message(message: Message):
    return message