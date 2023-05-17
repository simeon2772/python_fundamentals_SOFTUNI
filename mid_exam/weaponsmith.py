name_of_weapon = input().split('|')

while True:
    command = input()
    if command == "Done":
        print(f"You crafted {''.join(name_of_weapon)}!")

    current_command = command.split(' ')

    if current_command[0] == 'Add':
        particle = current_command[1]
        index = int(current_command[2])
        if 0 <= index < len(name_of_weapon):
            name_of_weapon[index] += particle
    elif current_command[0] == 'Remove':
        index_1 = int(current_command[1])
        if 0 <= index_1 < len(name_of_weapon):
            del name_of_weapon[index_1]
    elif current_command == 'Check Even':
        for index in name_of_weapon:
            if index % 2 == 0:
                print(index.split())
    elif current_command[0] == 'Check Odd':
        for index in name_of_weapon:
            if index % 2 != 0:
                print(''.join(index))