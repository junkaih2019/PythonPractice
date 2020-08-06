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
print("I can only invite 2 guests.")
Sorry_word = ", I'm sorry to tell you that we can't have your attendance."
print(guest[-1] + Sorry_word)
guest.pop()
print(guest[-1] + Sorry_word)
guest.pop()
print(guest[-1] + Sorry_word)
guest.pop()
print(guest[-1] + Sorry_word)
guest.pop()
del guest[0]
del guest[0]
print(guest)
