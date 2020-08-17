reason = input("Why you like programming?\nEnter q to quit.")
while True:
    if reason == 'q':
        break
    else:
        with open("reason.txt",'a+') as reason_file:
            reason_file.write(reason + '\n')
        reason = input()