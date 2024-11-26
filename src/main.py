from fastapi import FastAPI
from src.setting import Settings

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Hello, World!",
        "current_model": Settings().LLM_MODEL
    }
