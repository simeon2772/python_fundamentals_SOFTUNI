number_index = int(input())
count_of_positive = 0
sum_of_negatives = 0
positive_list = []
negative_list = []
for number in range(number_index):
    current_number = int(input())
    if current_number >= 0:
        positive_list.append(current_number)
        count_of_positive += 1
    else:
        negative_list.append(current_number)
        sum_of_negatives += current_number

print(positive_list)
print(negative_list)
print(f"Count of positives: {count_of_positive}")
print(f"Sum of negatives: {sum_of_negatives}")
