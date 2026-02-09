import os
import sys

KEYWORDS_TO_LANGS = {
  "C/C++": [
    "#include",
    "#define"
  ],
  "PHP": [
    "<?php"
  ],
  "HTML": [
    "<html",
    "<body",
    "<div"
  ],
  "Python": [
    "import",
    "def"
  ],
}

DIR_TO_SKIP = [
  ".git",
  "__pycache__",
  "venv",
  "node_modules",
  "build",
  "dist",
  "lib",
  "lib64",
  "refs",
  "origin",
  "36",
  "remotes",
  "localpycs"
]

def detect_lang_by_content(path):
  if not os.path.isfile(path):
    print("This script only works with files.")
    return
  
  with open(path, "rb") as file:
    file_content = file.read()

    for lang, keywords in KEYWORDS_TO_LANGS.items():
      for keyword in keywords:
        if keyword.encode() in file_content:
          return lang
  return None

def get_files(path):
  paths = os.walk(path)
  langs = set()

  for root, dirs, files in paths:
    if any([directory in DIR_TO_SKIP for directory in dirs]):
      continue
  
    for file in files:
      file_path = os.path.join(root, file)
      lang = detect_lang_by_content(file_path)
      if lang:
        langs.add(lang)

  print("Detected languages: ", langs)

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python detect-lang-by-content.py <file_path>")
    sys.exit(1)

  path = sys.argv[1]
  get_files(path)