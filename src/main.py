from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/start/{taille}")
async def start(taille: int):
    return {i+1: True for i in range(taille**2)}
