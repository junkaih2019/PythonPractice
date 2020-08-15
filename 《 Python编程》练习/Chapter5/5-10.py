current_users = ["li", "wang", "zack", "jack", "dam"]
new_users = ["tang", "tan", "zack", "Jack", "kim"]
for user in new_users:
    if user.lower() in current_users:
        print("You have to find another name.")
    else:
        print("Unused user name.")
