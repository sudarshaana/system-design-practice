import os
import sys

from serverless.dockerizer import build_all_functions

TEMPLATE_PATH = "./templates/function_template.py"
FUNCTIONS_DIR = "./functions"

def create_function(name):
    function_dir = os.path.join(FUNCTIONS_DIR, name)

    if os.path.exists(function_dir):
        print(f"x Function '{name}' already exists.")
        return

    os.makedirs(function_dir)
    print(f"+ Created directory: {function_dir}")

    # Copy and replace in function.py
    with open(TEMPLATE_PATH) as f:
        template = f.read().replace("{{function_name}}", name)

    with open(os.path.join(function_dir, "function.py"), "w") as f:
        f.write(template)
        print(f"+ Created function.py")

    # Write Dockerfile
    with open(os.path.join(function_dir, "Dockerfile"), "w") as f:
        f.write(f"""FROM python:3.10-slim
WORKDIR /app
COPY function.py .
ENTRYPOINT [\"python\", \"function.py\"]
""")
        print(f"+ Created Dockerfile")

    print(f"== Function '{name}' scaffolded successfully!")

    build_all_functions()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_function.py <FunctionName>")
        sys.exit(1)

    func_name = sys.argv[1]
    create_function(func_name)
