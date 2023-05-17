from math import ceil

number_of_people = int(input())
capacity = int(input())

elevator_rounds = ceil(number_of_people / capacity)

print(elevator_rounds)