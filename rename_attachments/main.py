import re
import os

ATTACHMENTS_PATH = ""
NOT_ALLOWED_CHARACTERS = re.compile(r'[^a-zA-Z0-9_#,.+\-]')

def sanitize_attachment_name(filename):
  name, ext = os.path.splitext(filename)
  clean_name = NOT_ALLOWED_CHARACTERS.sub("", name)
  return clean_name + ext

def get_attachments_with_incorrect_name(log_file):
  paths = os.walk(ATTACHMENTS_PATH)

  for root, _, files in paths:
    for x in files:
      attachment_path = os.path.join(root, x)
      allowed_characters_pattern = re.compile(r'^[a-zA-Z0-9_#,.+\-]+$')

      if not allowed_characters_pattern.match(x):
        sanitized_name = sanitize_attachment_name(x)
        attachment_path_sanitized = os.path.join(root, sanitized_name)

        if not os.path.exists(attachment_path_sanitized):
          os.rename(attachment_path, attachment_path_sanitized)
          log = f"RENAMED {attachment_path} TO {attachment_path_sanitized}"
          log_file.write(log + "\n")
          print(log)

if __name__ == "__main__":
  try:
    if os.path.exists("log"):
      os.remove("log")
    with open("log", "w", encoding="utf-8") as log_file:
      get_attachments_with_incorrect_name(log_file)
  except KeyboardInterrupt:
    pass
