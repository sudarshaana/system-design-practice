import subprocess
import json

def run_function_container(event_path):
    with open(event_path) as f:
        event_data = f.read()

    try:
        parsed = json.loads(event_data)
    except json.JSONDecodeError:
        print(f"[ERROR] Invalid JSON in {event_path}")
        return

    function_name = parsed.get("function")
    if not function_name:
        print(f"[SKIP] No 'function' key found in {event_path}")
        return

    container_name = f"local-func-{function_name}"
    print(f"[INFO] Triggering container: {container_name}")

    result = subprocess.run(
        ["docker", "run", "-i", container_name],
        input=event_data.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    if result.returncode != 0:
        print(f"[ERROR] Container failed:\n{result.stderr.decode()}")
        return

    print(f"[SUCCESS] {event_path} processed")
    print(result.stdout.decode())