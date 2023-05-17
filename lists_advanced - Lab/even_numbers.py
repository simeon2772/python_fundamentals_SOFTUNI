numbers = input().split(', ')
lst = []
for number in numbers:
    if int(number) % 2 == 0:
        lst.append(numbers.index(number))
print(lst)