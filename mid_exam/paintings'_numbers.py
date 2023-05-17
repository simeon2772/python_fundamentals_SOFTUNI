painting_numbers = input().split()
lst_painting_numbers = []
for number in painting_numbers:
    lst_painting_numbers.append(int(number))


while True:
    command = input()
    if command == "END":
        print(''.join(str(lst_painting_numbers)))

    current_command = command.split()

    if current_command[0] == "Change":
        painting_number = int(current_command[1])
        new_number = int(current_command[2])
        if painting_number < len(lst_painting_numbers):
            lst_painting_numbers[painting_number] = new_number
    elif current_command[0] == "Hide":
        painting_number___ = int(current_command[1])
        if painting_number___ in lst_painting_numbers:
            lst_painting_numbers.remove(painting_number___)
    elif current_command[0] == "Switch":
        painting_number_1 = int(current_command[1])
        painting_number_2 = int(current_command[2])
        if painting_number_1 not in lst_painting_numbers and painting_number_2 not in lst_painting_numbers:
            lst_painting_numbers[painting_number_1], lst_painting_numbers[painting_number_2]\
                = lst_painting_numbers[painting_number_2], lst_painting_numbers[painting_number_1]
    elif current_command[0] == "Insert":
        index = int(current_command[1])
        painting_number__ = int(current_command[2])
        if 0 <= index + 1 < len(lst_painting_numbers):
            lst_painting_numbers[index + 1] = painting_number__
    elif current_command[0] == "Reverse":
        lst_painting_numbers = lst_painting_numbers[::-1]

