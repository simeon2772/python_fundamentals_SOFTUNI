iterations = int(input())
integer_list = []
filtered = []

for numbers in range(iterations):
    current_number = int(input())
    integer_list.append(current_number)
command = input()
if command == 'even':
    for number in integer_list:
        if number % 2 == 0:
            filtered.append(number)
elif command == 'odd':
    for number in integer_list:
        if number % 2 != 0:
            filtered.append(number)
elif command == 'positive':
    for number in integer_list:
        if number >= 0:
            filtered.append(number)
elif command == 'negative':
    for number in integer_list:
        if number < 0:
            filtered.append(number)
print(filtered)