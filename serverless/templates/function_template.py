import sys, json

def handler(event):
    # TODO: implement logic for {{function_name}}
    return {"message": "Hello from {{function_name}}"}

if __name__ == "__main__":
    event = json.loads(sys.stdin.read())
    print(json.dumps(handler(event)))
