import sys, json

def handler(event):

    name = event.get("name", "World")
    email = event.get("email", "email@example.com")

    return {"message": f"sent email to {name} ({email})!"}

if __name__ == "__main__":
    event = json.loads(sys.stdin.read())
    print(json.dumps(handler(event)))
