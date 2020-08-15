user_name = ['admin', 'li', 'wang', 'yang', 'qin']
for user in user_name:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user + ",thank you for logging in again")
