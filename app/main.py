from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

assignments = []

class Assignment(BaseModel):
    title: str
    module: str
    due_date: str
    priority: str # low, medium, high

@app.get("/")
def home():
    return {"message": "Assignment Tracker API"}

@app.get("/assignments")
def get_assignments():
    return assignments

@app.post("/assignments")
def create_assignment(assignment: Assignment):
    assignments.append(assignment)
    return assignment

@app.get("/assignments/priority/{level}")
def get_assignemnts_by_priority(level: str):
    filtered = []

    for a in assignments:
        if a["priority"] == level:
            filtered.append(a)

    return filtered

@app.get("/assignemnts/module/{module_name}")
def get_assignments_by_module(module_name: str):
    filtered_mods = []

    for b in assignments:
        if b["module"] == module_name:
        filtered_mods.append(a)

    return filtered_mods
