import inotify.adapters
import os
import sys

def watch_dir(path):
  if not os.path.isdir(path):
    print(f"Error: {path} is not a valid directory.")
    return
  
  i = inotify.adapters.Inotify()
  i.add_watch(path)

  print(f"Watching directory: {path}")
  try:
    for event in i.event_gen(yield_nones=False):
      (_, type_names, path, filename) = event
      full_path = os.path.join(path, filename)
      if "IN_ISDIR" in type_names:
        pass
      elif "IN_CREATE" in type_names:
        print(f"File created: {full_path}")
      elif "IN_MODIFY" in type_names:
        print(f"File modified: {full_path}")
  except KeyboardInterrupt:
    pass
  finally:
    i.remove_watch(path)
    print(f"Stopped watching directory: {path}")

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python main.py <directory_to_watch>")
    sys.exit(1)

  watch_dir(sys.argv[1])