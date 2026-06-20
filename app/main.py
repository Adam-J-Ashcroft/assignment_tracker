from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Assignment Tracker API"}