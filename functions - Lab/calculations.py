def calculation(command, first_number, second_number):
    if command == "multiply":
        return first_number * second_number
    elif command == "divide":
        return first_number // second_number
    elif command == "add":
        return first_number + second_number
    elif command == "subtract":
        return first_number - second_number


command = input()
first_number = int(input())
second_number = int(input())
print(calculation(command, first_number, second_number))


