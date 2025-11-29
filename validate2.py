import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# \w == [a-zA-Z0-9_] -- word char commonly known as alphanumeric symbol or underscore.
# \W -- everything but not a word char.
# re.IGNORECASE -- to ignore the uppercase
# to ignore uppercase letters -- can also be written -- .strip().lowercase() or email.lowercase()