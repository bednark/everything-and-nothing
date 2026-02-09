import sys
import os
from pathlib import Path

def list_with_os(path):
  result = os.walk(path)
  print("Listing directories with os.walk:")

  for root, _, _ in result:
    if root == path:
      continue
    print(f"Directory: {root}")

def list_with_pathlib(path):
  result = Path(path).rglob("*")
  print("Listing directories with pathlib:")

  for item in result:
    if item.is_dir():
      print(f"Directory: {item}")

def list_resursively(path):
  result = os.listdir(path)

  for item in result:
    item_path = os.path.join(path, item)
    if os.path.isdir(item_path):
      print(f"Directory: {item_path}")
      list_resursively(item_path)


if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Usage: python listing-directories.py <directory>")
    sys.exit(1)

  path = sys.argv[1]
  print("OS way:")
  list_with_os(path)

  print("\nPathlib way:")
  list_with_pathlib(path)

  print("\nRecursive way:")
  list_resursively(path)