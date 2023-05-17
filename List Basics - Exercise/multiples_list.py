factor = int(input())
count = int(input())
list_of_numbers = []

for numbers in range(1, count + 1):
    list_of_numbers.append(factor * numbers)
print(list_of_numbers)