import sys
import os

def count_lines(path):
  _, ext = os.path.splitext(path)

  if ext != ".py":
    print("This script only counts lines in Python files.")
    return

  with open(path, "rb") as file:
    file_content = file.read()
    lines = file_content.splitlines()

    file_content = [
      stripped for line in lines
        if (stripped := line.lstrip())
          and not (stripped.startswith(b"#") or stripped == b"")
    ]

    print(f"Source code has: {len(file_content)} lines.")

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python lines-counter.py <file_path>")
    sys.exit(1)

  path = sys.argv[1]
  count_lines(path)