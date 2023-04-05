import json


rocky = {}

rocky["name"] = "Rocky Balboa"
rocky["age"] = 30
rocky["profession"] = ["Boxer", "Trainer", "TV Commercials"]

json.dump(rocky, open("/home/ubuntu/environment/test/rocky.json", "w"))

rocky_II = {}

rocky_II = json.load(open("/home/ubuntu/environment/test/rocky.json"))

print(rocky_II)