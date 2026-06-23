from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

assignments = [
    {"title": "Maths", "module": "CS101", "completed": True},
    {"title": "Essay", "module": "ENG101", "completed": False},
    {"title": "Physics", "module": "CS101", "completed": True},
    {"title": "Programming", "module": "CS102", "completed": False}
    ]

class Assignment(BaseModel):
    title: str
    module: str
    due_date: str
    completed: bool 

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
def get_assignments_by_priority(level: str):
    filtered = []

    for a in assignments:
        if a["priority"] == level:
            filtered.append(a)

    return filtered

@app.get("/assignments/module/{module_name}")
def get_assignments_by_module(module_name: str):
    filtered_mods = []

    for b in assignments:
        if b["module"] == module_name:
            filtered_mods.append(b)

    return filtered_mods

@app.get("/assignments/stats")
def get_stats():
    completed = []

    for a in assignments:
        if a["completed"]:
            completed.append(a["title"])

    return {
        "total_assignments": len(assignments),
        "completed_assignments": completed
    }

@app.get("/assignments/{title}")
def get_assignments_by_title(title: str):
    assignment_specific = []

    for a in assignments:
        if a["title"] == title:
            assignment_specific.append(a)
    
    return assignment_specific

@app.get("/assignments/dashboard")
def get_dashboard_stats():
    total = 0
    total_completed = 0

    for a in assignments:
        total += 1
        if a["completed"]:
            total_completed += 1 
    
    total_incomplete = total - total_completed

    if total == 0:
        completion_rate = 0
    else:
        completion_rate = (total_completed/total) * 100

    return {
        "total_assignments": total,
        "completed_assignments": total_completed,
        "incomplete_assignments": total_incomplete,
        "completion_rate": completion_rate
    }
    
@app.get("/assignments/modules")
def get_number_remaining():
    module_counts = {}

    for a in assignments:
        module_name = a["module"]
        module_counts[module_name] = module_counts.get(module_name, 0) + 1

    
            
