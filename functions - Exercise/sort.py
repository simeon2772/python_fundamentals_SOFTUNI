numbers = input().split()
number_lst = []
for current_number in numbers:
    converted_numbers = int(current_number)
    number_lst.append(converted_numbers)
result = sorted(number_lst)
print(result)