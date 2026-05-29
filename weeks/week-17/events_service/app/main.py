from fastapi import FastAPI

app = FastAPI()

events = [
    {"id": 1, "name": "Conference", "location": "Berlin"},
    {"id": 2, "name": "Meetup", "location": "Munich"},
]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/events")
def get_events():
    return events


@app.post("/api/events")
def create_event(event: dict):
    events.append(event)
    return event


@app.put("/api/events/{event_id}")
def update_event(event_id: int, updated_event: dict):
    for index, event in enumerate(events):
        if event.get("id") == event_id:
            updated_event["id"] = event_id
            events[index] = updated_event
            return updated_event
    return {"error": "Event not found"}


@app.delete("/api/events/{event_id}")
def delete_event(event_id: int):
    for index, event in enumerate(events):
        if event.get("id") == event_id:
            deleted_event = events.pop(index)
            return deleted_event
    return {"error": "Event not found"}
