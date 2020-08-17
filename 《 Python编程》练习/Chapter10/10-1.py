with open("learning_python.txt") as file_py:
    contents = file_py.read()
    print(contents)
with open("learning_python.txt") as file_py:
    for content in file_py:
        print(content.rstrip())
with open("learning_python.txt") as file_py:
    lines = file_py.readlines()
for line in lines:
    print(line.rstrip())
