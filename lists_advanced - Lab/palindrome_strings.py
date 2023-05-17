words = input().split()
palindrome = input()

sequence_of_palindromes = []

for word in words:
    if word == word[::-1]:
        sequence_of_palindromes.append(word)

print(sequence_of_palindromes)
print(f"Found palindrome {words.count(palindrome)} times")