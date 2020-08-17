name = input("Enter your name: ")
file_name = "guest.txt"
with open(file_name,'w') as file:
    file.write(name)
