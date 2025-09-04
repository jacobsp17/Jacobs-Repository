message = "This is THE secret message!!!"

# write message to the file
with open('secret_message.txt', 'w') as file:
    file.write(message)

# remove message from the file and notify the user
with open('secret_message.txt', 'r+') as file:
    original_message = file.read()
    file.seek(0)
    flag = "this message has been unsent"
    file.write(flag)
    file.truncate(28)

    print("Original message was:", original_message)
