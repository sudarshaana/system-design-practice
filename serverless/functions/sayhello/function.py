import sys, json

def handler(event):
    # TODO: implement logic for sayhello
    return {"message": "Hello from sayhello"}

if __name__ == "__main__":
    event = json.loads(sys.stdin.read())
    print(json.dumps(handler(event)))
