import re

email = input("What's your email? ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

# Regular Expressions or Regexes is a pattern to match other data.
# r -- raw string -- tell the python not intrepet \ in usual way instead to pass it.
# [^@] -- syntax -- anything except @ sign.
# [a-z] -- you mean letters from a to z to be written in email
# [a-zA-Z] -- to include uppercase letters too.
# [a-zA-Z0-9_] -- to include numbers from 0 to 9 as well as underscore.
# re.search(pattern, string, flags=0)