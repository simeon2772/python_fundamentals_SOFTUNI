numbers = input().split()
filtered_numbers = []
for number in numbers:
    rounded_numbers = round(float(number))
    filtered_numbers.append(rounded_numbers)
print(filtered_numbers)