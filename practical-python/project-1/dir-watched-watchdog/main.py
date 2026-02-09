import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import sys

class MyEventHandler(FileSystemEventHandler):  
  def on_created(self, event) -> None:
    print(f"File created: {event.src_path}")

  def on_modified(self, event) -> None:
    if event.is_directory:
      return
    print(f"File modified: {event.src_path}")
  
  def on_deleted(self, event) -> None:
    print(f"File deleted: {event.src_path}")

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python main.py [src_path]")
    sys.exit(1)

  src_path = sys.argv[1]
  print(f"Watching directory: {src_path}")

  event_handler = MyEventHandler()
  observer = Observer()
  observer.schedule(event_handler, src_path, recursive=True)
  observer.start()
  try:
    while True:
      pass
  except KeyboardInterrupt:
    pass
  finally:
    observer.stop()
    observer.join()