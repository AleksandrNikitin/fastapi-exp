from fastapi import FastAPI

app = FastAPI()

@app.get("/show")
async def root():
    return {"message": "Hello World"}