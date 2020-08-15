prompt = "If you could visit one place in the world, where would you go?\n"
active = True
result = []
while active:
    place = input(prompt)
    result.append(place)

    repeat = input("Would you like to say another place? (yes/no)\n")
    if repeat == 'no':
        active = False

for place in result:
    print(place)