from fastapi import FastAPI

app = FastAPI()

events = [{"id": 1, "name": "Conference", "location": "Berlin"},
    {"id": 2, "name": "Meetup", "location": "Munich"}]

@app.get("/api/events")
def get_events():
    return events

@app.post("/api/events")
def create_event(event: dict):
    events.append(event)
    return event