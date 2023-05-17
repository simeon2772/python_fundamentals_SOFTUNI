numbers = input().split()
number_lst = []
for current_number in numbers:
    converted_numbers = int(current_number)
    number_lst.append(converted_numbers)

minimum_number = min(number_lst)
maximum_number = max(number_lst)
sum_all_numbers = sum(number_lst)

print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_all_numbers}")