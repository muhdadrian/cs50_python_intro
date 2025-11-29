import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json() #grabbing the json object
for result in o["results"]: #results is the key in the dictionary, the result key is a list
    print(result["trackName"]) #trackName is the key in the dictionary

"""
-response variable is making http request
-entity=song&limit=50&term= -- the 50 means produces 50 songs
-variable o is for object
-break is used to break out things in loop, 
while sys.exit() is used to terminate whole of the program.
-to better understand the results and trackname in the loop above, try running itunes2.py
and look at the dictionary. 
"""
