import requests
import sys

if len(sys.argv) != 2: #error checking -- name of the file and name of the band.
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())

# in command-line: python itunes.py weezer -- test purpose
#python convert the json file sent by apple into python dictionary
# pip install requests