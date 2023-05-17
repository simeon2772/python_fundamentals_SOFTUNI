word = input()

while True:
    command = input().split()
    if command[0] == "Easter":
        break

    if command[0] == "Replace":
        current_char = command[1]
        new_char = command[2]
        word = word.replace(current_char, new_char)
        print(word)
    elif command[0] == "Remove":
        substring = command[1]
        word = word.replace(substring, "")
        print(word)
    elif command[0] == "Includes":
        string_ = command[1]
        if string_ in word:
            print("True")
        else:
            print("False")
    elif command[0] == "Change":
        possible_command = command[1]
        if possible_command == "Lower":
            word = word.lower()
            print(word)
        else:
            word = word.upper()
            print(word)
    elif command[0] == "Reverse":
        start_index = int(command[1])
        end_index = int(command[2])
        if len(word) < start_index or len(word) < end_index:
            continue
        substring = word[start_index:end_index + 1]
        reversed_string = substring[::-1]
        print(reversed_string)


