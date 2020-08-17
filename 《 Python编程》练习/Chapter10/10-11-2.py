import json

try:
    with open("fav_num.json") as f:
        num = json.load(f)
except FileNotFoundError:
    pass
else:
    print(num)
