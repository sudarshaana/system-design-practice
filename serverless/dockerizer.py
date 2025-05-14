import os
import subprocess

FUNCTIONS_DIR = "./functions"

def build_function_docker(function_name):
    func_dir = os.path.join(FUNCTIONS_DIR, function_name)
    dockerfile_path = os.path.join(func_dir, "Dockerfile")

    # Create Dockerfile if not exists
    if not os.path.exists(dockerfile_path):
        with open(dockerfile_path, "w") as f:
            f.write(f"""FROM python:3.10-slim
WORKDIR /app
COPY function.py .
ENTRYPOINT [\"python\", \"function.py\"]
""")

    # Build docker image
    tag = f"local-func-{function_name}"
    print(f"[BUILDING] Docker image: {tag}")
    subprocess.run(["docker", "build", "-t", tag, "."], cwd=func_dir)

def build_all_functions():
    for fn in os.listdir(FUNCTIONS_DIR):
        if os.path.isdir(os.path.join(FUNCTIONS_DIR, fn)):
            build_function_docker(fn)

if __name__ == "__main__":
    build_all_functions()
