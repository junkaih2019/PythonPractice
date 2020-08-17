file_name = "learning_python.txt"
try:
    with open(file_name) as f:
        contents = f.read()
except FileNotFoundError:
    print("File not exit.")
else:
    num = contents.lower().count('python')
    print(num)
