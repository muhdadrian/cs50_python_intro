url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")

# This will print all for e.g: My username is davidjmalan.
# Our goal is to get the username only.