number_string = input()

number_string = ''.join(sorted(number_string, reverse=True))
print(number_string)