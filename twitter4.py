import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))

# Refined version from twitter3.py
# if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE) -- this is the previous code replaced by the above code.