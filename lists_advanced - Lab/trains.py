number_of_wagons = int(input())
train = [0] * number_of_wagons

while True:
    command = input()
    if command == "End":
        print(train)
        break

    current_command = command.split()

    if current_command[0] == "add":
        people = int(current_command[1])
        train[-1] += people
    elif current_command[0] == "insert":
        index = int(current_command[1])
        people = int(current_command[2])
        train[index] += people
    elif current_command[0] == "leave":
        index = int(current_command[1])
        people = int(current_command[2])
        train[index] -= people
