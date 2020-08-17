while True:
    name = input("Enter your name, enter q to quit.\n")
    if name == 'q':
        break
    with open("guest_book.txt", 'a+') as file:
        file.write(name + '\n')