text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
result = [char for char in text if char not in vowels]
print("".join(result))
