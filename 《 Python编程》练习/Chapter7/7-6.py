#2
good = True
while good:
    pizza_material = input("Enter a kind of pizza material, enter 'quit' to quit.\n")
    if (pizza_material != 'quit'):
        print("We will add " + pizza_material + " to our new pizza!\n")
    else:
        break

