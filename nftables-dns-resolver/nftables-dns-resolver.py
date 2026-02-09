import os
import sys
import socket

DOMAINS_TO_RESOLVE = [
    "pypi.org",
    "index.docker.io",
    "registry-1.docker.io",
    "api.segment.io",
    "cdn.segment.com",
    "notify.bugsnag.com",
    "sessions.bugsnag.com",
    "auth.docker.io",
    "cdn.auth0.com",
    "login.docker.io",
    "desktop.docker.com",
    "hub.docker.com",
    "production.cloudflare.docker.com",
    "docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com",
    "docker-pinata-support.s3.amazonaws.com",
    "api.dso.docker.com",
    "api.docker.com"
]

def resolve_domains():
  result = []
  for domain in DOMAINS_TO_RESOLVE:
    try:
      ips = socket.gethostbyname_ex(domain)
      if not ips:
        continue
      result += ips[2]
    except Exception as e:
      print(f"Error resolving {domain}: {e}")
      continue
  if not result:
    return set("1.2.3.4")
  return set(result)

def update_domains(path):
  addresses = ", ".join(resolve_domains())
  new_line = f"define repo_addresses = {{ {addresses} }}\n"

  with open(path, "r") as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
      if line.startswith("define repo_addresses"):
        lines[i] = new_line
        break

  with open(path, "w") as file:
    file.writelines(lines)

  os.system("systemctl reload nftables")

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python script.py <path>")
    sys.exit(1)

  path = sys.argv[1]
  update_domains(path)