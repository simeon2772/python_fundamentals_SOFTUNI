encrypted_message = input()

while True:
    commands = input().split("|")
    if commands[0] == "Decode":
        break

    if commands[0] == "Move":
        number_of_letters_to_move = int(commands[1])
        encrypted_message = encrypted_message[number_of_letters_to_move:] + \
                  encrypted_message[:number_of_letters_to_move]
    if commands[0] == "Insert":
        index = int(commands[1])
        value = commands[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    if commands[0].startswith("ChangeAll"):
        substring = commands[1]
        replacement = commands[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

print(f"The decrypted message is: {encrypted_message}")
