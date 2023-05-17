string_input = input().split()
numbers = []

for element in string_input:
    current_number = -int(element)
    numbers.append(current_number)
print(numbers)

