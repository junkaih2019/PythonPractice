file_name = ["cats.txt", "dogs.txt"]
try:
    for file  in file_name:
        with open(file) as f:
            content = f.read()
        print(content)
except FileNotFoundError:
    print("Please Enter the right file name.")