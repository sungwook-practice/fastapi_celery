from fastapi import FastAPI
from worker import celery

app = FastAPI()


@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.get("/celery")
def trigger_celery():
  task = celery.send_task("tasks.long_running_task", args=[], countdown=5)
  task.get()

  return {"task_id": task.id}
