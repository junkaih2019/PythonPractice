# based on 3-5.py
guest = ['li', 'wang', 'tan']
invitation_word = ", would you like to take part in the party?"
print(guest[0].title() + invitation_word)
print(guest[1].title() + invitation_word)
print(guest[2].title() + invitation_word)
print(guest[2].title() + " can't attend.")
del guest[2]
guest.insert(2, "wen")
print(guest[0].title() + invitation_word)
print(guest[1].title() + invitation_word)
print(guest[2].title() + invitation_word)
print("Now I have invited " + str(len(guest)) + " guests.")
