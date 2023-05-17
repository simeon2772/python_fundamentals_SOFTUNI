text = input()

digits, letters, others = [], [], []

for symbol in text:
    if symbol.isdigit():
        digits.append(symbol)
    elif symbol.isalpha():
        letters.append(symbol)
    else:
        others.append(symbol)

print(''.join(digits))
print(''.join(letters))
print(''.join(others))
