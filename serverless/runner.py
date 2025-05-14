import subprocess

def run_function_container(event_path):
    with open(event_path, 'r') as f:
        event_data = f.read()

    result = subprocess.run(
        ["docker", "run", "-i", "local-serverless-function"],
        input=event_data.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    if result.returncode != 0:
        print(f"Error: {result.stdout.decode()}")
        return

    print(f"OK. Processed event {event_path}")
    print(result.stdout.decode())
