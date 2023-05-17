string_number = input().split(', ')
numbers = []
for number in string_number:
    numbers.append(int(number))

element = 0

for number_ in numbers:
    if number_ == element:
        del numbers[numbers.index(element)]
        numbers.append(number_)

print(numbers)