from pygments.lexers import guess_lexer
import os
import sys

def detect_lang(path):
  if not os.path.isfile(path):
    print("This script only works with files.")
    return None
  
  with open(path, "r") as file:
    file_content = file.read()
    lexer = guess_lexer(file_content)

    if lexer:
      return lexer.name
    else:
      return None
    
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