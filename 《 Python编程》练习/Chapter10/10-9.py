file_name = ["cat.txt", "dogs.txt"]
try:
    for file  in file_name:
        with open(file) as f:
            content = f.read()
        print(content)
except FileNotFoundError:
    pass