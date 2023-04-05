import json
import requests

url = "https://api.datamuse.com/words?rel_trg=cow"

json_cow = requests.get(url).text

dict_cow = json.loads(json_cow)


print(json_cow)

print(dict_cow[0]["score"])

print(dict_cow[-1]["word"])




