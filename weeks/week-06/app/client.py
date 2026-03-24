PROJECT_CODE = "events-s06"

URL = "http://localhost:8237/graphql"



def build_payload(query: str, variables: dict | None = None) -> dict:
    payload = {
        "query": query
    }
    if variables:
        payload["variables"] = variables
    return payload



def send_request(payload: dict):
    import requests  # важно: импорт внутри функции
    response = requests.post(URL, json=payload)
    return response.json()



def handle_response(response: dict):
    if "errors" in response:
        print("Errors:")
        for err in response["errors"]:
            print(err)
    else:
        print("Data:")
        print(response.get("data"))



def get_events():
    query = """
    query {
        events {
            id
            name
            location
        }
    }
    """
    payload = build_payload(query)
    response = send_request(payload)
    handle_response(response)



def create_event(name: str, location: str):
    mutation = """
    mutation($name: String!, $location: String!) {
        createEvent(name: $name, location: $location) {
            id
            name
            location
        }
    }
    """
    variables = {
        "name": name,
        "location": location
    }
    payload = build_payload(mutation, variables)
    response = send_request(payload)
    handle_response(response)



if __name__ == "__main__":
    create_event("Conference", "Amsterdam")
    get_events()