import os
import re
import sys

LANGS_REGEX = {
  "C/C++": [
    r"#include.*",
    r"#define.*"
  ],
  "PHP": [
    r"<\?php.*"
  ],
  "HTML": [
    r"<html.*",
    r"<body.*",
    r"<div.*"
  ],
  "Python": [
    r"import.*",
    r"def.*"
    r"for.*in.*",
  ],
}

def detect_lang(path):
  if not os.path.isfile(path):
    print("This script only works with files.")
    return None
  
  with open(path, "r") as file:
    file_content = file.readlines()

    for lang, regexes in LANGS_REGEX.items():
      for regex in regexes:
        for line in file_content:
          line = line.strip()
          if not line:
            continue
          if re.search(regex, line):
            return lang
        
if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python script.py <path>")
    sys.exit(1)

  path = sys.argv[1]
  lang = detect_lang(path)
  
  if lang:
    print(f"Detected language: {lang}")
  else:
    print("No language detected.")
  path = sys.argv[1]