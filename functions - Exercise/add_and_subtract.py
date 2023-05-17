def sum_numbers(first_num, second_num):
    return first_num + second_num


def subtract(sum_numbers, third_num):
    return sum_numbers - third_num


def add_and_subtract(sum_numbers, subtract):
    pass


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(subtract(sum_numbers(first_num, second_num), third_num))
