from fastapi import FastAPI

app = FastAPI()

data = []

@app.get("/notifications")
def get_notifications():
    return data

@app.post("/notifications")
def create_notification(notification: dict):
    data.append(notification)
    return notification