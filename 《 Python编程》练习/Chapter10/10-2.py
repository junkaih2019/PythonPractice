with open("learning_python.txt") as f:
    lines = f.readlines()
    for line in lines:
        print(line.rstrip().replace('Python', 'C'))
