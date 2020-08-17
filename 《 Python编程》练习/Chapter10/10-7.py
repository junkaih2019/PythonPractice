active = True
while active:
    try:
        x = input("Enter the first number: ")
        x = int(x)

        y = input("Enter the second number: ")
        y = int(y)
    except ValueError:
        print("Please Enter number.")
    else:
        active = False
        sum = x + y
        print("The sum of x and y is " + str(sum))
