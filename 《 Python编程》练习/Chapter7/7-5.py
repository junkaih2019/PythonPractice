prompt = "How old are you?"
prompt += "(Enter 'quit' to quit)\n"
active = True
while active:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("You are free to go.\n")
    elif age < 13:
        print("10$,pls.\n")
    elif age > 12:
        print("15$,pls.\n")
