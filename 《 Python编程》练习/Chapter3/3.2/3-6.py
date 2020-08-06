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
print("I find a bigger desk.")
guest.insert(0, "huang")
guest.insert(2, "mi")
guest.append("last")
print(guest[0].title() + invitation_word)
print(guest[1].title() + invitation_word)
print(guest[2].title() + invitation_word)
print(guest[3].title() + invitation_word)
print(guest[4].title() + invitation_word)
print(guest[5].title() + invitation_word)

