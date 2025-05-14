# Local Serverless CLI (Function Runner)

A lightweight local framework to simulate serverless computing using Docker containers and file-based event triggers — no cloud required!

---

## Features

- Scaffold new functions using a CLI (`create_function.py`)
- Auto-generate Dockerfiles and build function containers (`dockerizer.py`)
- Route `.json` events to corresponding function containers (`runner.py`)
- Watch an `events/` folder for changes and auto-trigger execution (`folder_watcher.py`)
- Supports both `on_created` and `on_modified` triggers


## To Create a new Function
```bash 
python create_function.py sayhello
```
## Start Script
```bash
python folder_watcher.py
```

## What does it do?
- Reads new file created or modification in `./event` folder
- Automatically create function and docker image to run execute the function

## Sample Event
```
{
  "function": "sendEmail",
  "name": "Sudarshan",
  "email": "sud@example.com"
}
```
Place in `./events/` to trigger the corresponding container.



## Future Ideas
- Add CLI support for build, run, watch
- Redis or API gateway trigger simulation
- Result logging to ./results/
- Retry on failure and cold start delay

## Requirements
- Python 3.8+
- Docker installed and running
- watchdog Python package:
  `pip install watchdog`