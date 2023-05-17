names = input().split(', ')
sorted_lst = sorted(names, key=lambda item: (-len(item), item))
print(sorted_lst)
