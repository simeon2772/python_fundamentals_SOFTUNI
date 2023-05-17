def even_numbers(sequence_numbers):
    for current_number in sequence_numbers:
        if int(current_number) % 2 == 0:
            number_lst.append(int(current_number))


number_lst = []
sequence_numbers = input().split()
result = filter(even_numbers(sequence_numbers), number_lst)
print(number_lst)
