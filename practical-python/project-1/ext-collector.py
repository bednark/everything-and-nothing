import sys
import os
from pathlib import Path

DIR_TO_SKIP = [
  ".git",
  "__pycache__",
  "venv",
  "node_modules",
]

def list_dirs(path):
  paths = os.listdir(path)
  files = []

  for item in paths:
    if item in DIR_TO_SKIP:
      continue

    item_path = os.path.join(path, item)
    if os.path.isdir(item_path):
      files = files + list_dirs(item_path)
    else:
      files.append(item_path)
  return files

def collect_exts(path):
  exts = set()
  files = list_dirs(path)

  for file in files:
    _, ext = os.path.splitext(file)
    if ext == "":
      ext = "UNKNOWN"
    exts.add(ext)

  print("Unique file extensions: ", exts)

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Usage: python ext-collector.py <directory>")
    sys.exit(1)

  path = sys.argv[1]
  collect_exts(path)