import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

#Pytohn code that pretend to be web browser

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

# print(json.dumps(response.json() , indent=2)) #Prints content of the reposne

res_ = response.json()

for result in res_["results"]:
    print(result["trackName"])
