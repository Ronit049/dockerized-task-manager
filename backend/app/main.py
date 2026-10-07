from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from bson import ObjectId

from .database import tasks_collection
from .models import TaskCreate, TaskUpdate


app = FastAPI(
    title="Dockerized Task Manager API",
    description="Simple Task Manager built with FastAPI, MongoDB and Docker",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def task_serializer(task):
    return {
        "id": str(task["_id"]),
        "title": task["title"],
        "description": task.get("description", ""),
        "completed": task.get("completed", False),
    }


@app.get("/")
def root():
    return {"message": "Dockerized Task Manager API is running 🚀"}


@app.get("/health")
def health():
    try:
        tasks_collection.database.client.admin.command("ping")
        return {"status": "healthy", "database": "connected"}
    except Exception:
        return {"status": "unhealthy", "database": "disconnected"}


@app.get("/tasks")
def get_tasks():
    tasks = tasks_collection.find().sort("_id", -1)
    return [task_serializer(task) for task in tasks]


@app.post("/tasks")
def create_task(task: TaskCreate):
    new_task = {
        "title": task.title,
        "description": task.description,
        "completed": False
    }

    result = tasks_collection.insert_one(new_task)
    created_task = tasks_collection.find_one({"_id": result.inserted_id})

    return task_serializer(created_task)


@app.put("/tasks/{task_id}")
def update_task(task_id: str, task: TaskUpdate):
    try:
        object_id = ObjectId(task_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid task ID")

    update_data = {
        key: value
        for key, value in task.model_dump().items()
        if value is not None
    }

    if not update_data:
        raise HTTPException(status_code=400, detail="No data provided for update")

    result = tasks_collection.update_one(
        {"_id": object_id},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")

    updated_task = tasks_collection.find_one({"_id": object_id})
    return task_serializer(updated_task)


@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    try:
        object_id = ObjectId(task_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid task ID")

    result = tasks_collection.delete_one({"_id": object_id})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted successfully"}
