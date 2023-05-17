def calculation(number):
    sum_of_even_nums = 0
    sum_of_odd_nums = 0
    for current_number in number:
        if int(current_number) % 2 == 0:
            sum_of_even_nums += int(current_number)
        else:
            sum_of_odd_nums += int(current_number)
    return sum_of_odd_nums, sum_of_even_nums


initial_number = input()
sum_of_odd_nums, sum_of_even_nums = calculation(initial_number)
print(f"Odd sum = {sum_of_odd_nums}, Even sum = {sum_of_even_nums}")
