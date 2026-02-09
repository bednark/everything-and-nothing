import os
import sys
import time

FILES_CACHE = {}

def get_files(path):
  files_to_print = []

  if not os.path.isdir(path):
    print("This script only works with directories.")
    return []
  
  for root, _, files in os.walk(path):
    for file in files:
      file_path = os.path.join(root, file)
      file_last_modified_ts = os.stat(file_path).st_mtime

      if file not in FILES_CACHE or FILES_CACHE[file] != file_last_modified_ts:
        FILES_CACHE[file] = file_last_modified_ts
        files_to_print.append(file_path)

  print(files_to_print)

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python script.py <path>")
    sys.exit(1)

  path = sys.argv[1]

  try:
    while True:
      get_files(path)
      time.sleep(1)
  except KeyboardInterrupt:
    sys.exit(0)