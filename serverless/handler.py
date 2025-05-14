import sys
import json


def handler(event):
    name = event.get("name", "World")
    return {"message": f"Hello, {name}!"}


if __name__ == "__main__":
    event = json.loads(sys.stdin.read())
    result = handler(event)
    print(json.dumps(result))
