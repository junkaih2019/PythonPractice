import json

try:
    num = input("What is your favorite number? ")
    num = int(num)
except ValueError:
    print("Please enter number.")
else:
    with open("fav_num.json", 'w') as f:
        json.dump(num, f)
