import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from runner import run_function_container

WATCH_FOLDER = "./events"
file_last_processed = {}

class EventFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        if event.src_path.endswith(".json"):
            print(f"[New File] {event.src_path}")
            run_function_container(event.src_path)

    def on_modified(self, event):
        if event.is_directory:
            return
        now = time.time()
        last = file_last_processed.get(event.src_path, 0)
        if now - last > 2:  # only allow once every 2 seconds
            if event.src_path.endswith(".json"):
                print(f"[Modified File] {event.src_path}")
                run_function_container(event.src_path)

if __name__ == "__main__":
    print(f"📁 Watching folder: {WATCH_FOLDER}")
    event_handler = EventFileHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_FOLDER, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
