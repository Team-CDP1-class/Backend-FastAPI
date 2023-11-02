from Backend.Prompt.filtering1 import Filtering
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}