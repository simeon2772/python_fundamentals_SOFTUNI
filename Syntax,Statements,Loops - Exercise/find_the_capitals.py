word = input()
lst = []
for index, letter in enumerate(word):
    if letter.isupper():
        lst.append(index)
print(lst)
