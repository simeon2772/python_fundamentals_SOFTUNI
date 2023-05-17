first_sequence = input().split(', ')
second_sequence = input().split(', ')
new_lst = []

for first_word in first_sequence:
    for second_word in second_sequence:
        if first_word in second_word and first_word not in new_lst:
            new_lst.append(first_word)
print(new_lst)