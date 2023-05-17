numbers = input().split()
lst_numbers = []
for number in numbers:
    numbers_converted = abs(float(number))
    lst_numbers.append(numbers_converted)

print(lst_numbers)
