number = int(input())
zero_or_one = int(input())

counter = 0  # counter for zeros and ones


while number > 0:
    leftover = number % 2
    if leftover == number:
        counter += 1
    number = number // 2
print(counter)