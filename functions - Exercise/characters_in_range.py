def between_ascii(first, second):
    char_lst = []
    for current_char in range(ord(first) + 1, ord(second)):
        char_lst.append(chr(current_char))
    return char_lst


first_character = input()
second_character = input()
result = between_ascii(first_character,second_character)
print(' '.join(result))
