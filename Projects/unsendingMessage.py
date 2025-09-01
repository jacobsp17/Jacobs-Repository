message = "This is THE secret message!!!"

with open('secret_message.txt', 'w') as file:
    file.write(message)

with open('secret_message.txt', 'r+') as file:
    original_message = file.read()
    file.seek(0)
    flag = "this message has been unsent "
    file.write(flag)
    file.truncate(28)

    print("Original message was:", original_message)