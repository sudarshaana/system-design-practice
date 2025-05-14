import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from runner import run_function_container

WATCH_FOLDER = "./events"


class EventFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        if event.src_path.endswith(".json"):
            print(f"+ Detected new event file: {event.src_path}")
            run_function_container(event.src_path)

    def on_modified(self, event):
        if event.is_directory:
            return

        if event.src_path.endswith(".json"):
            print(f"-+Detected Edit event: {event.src_path}")
            run_function_container(event.src_path)


if __name__ == "__main__":

    print(f"Watching folder: {WATCH_FOLDER}")

    event_handler = EventFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_FOLDER, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
