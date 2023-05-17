number_of_rooms = int(input())

for room in range(1, number_of_rooms + 1):
    current_command = input().split()
    chairs = current_command[0]
    visitors = int(current_command[1])
    chair_number = 0
    for chair in chairs:
        if chair == "X":
            chair_number += 1
    free_chairs = abs(chair_number) - abs(visitors)
    if chair_number < visitors:
        print(f"{visitors - chair_number} more chairs needed in room {room}")
    else:
        print(f"Game On, {free_chairs} free chairs left")
