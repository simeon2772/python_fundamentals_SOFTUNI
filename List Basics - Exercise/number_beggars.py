money_for_beggars = input().split(", ")
beggars = int(input())
numbers_money_for_beggars = []
for elements in money_for_beggars:
    numbers_money_for_beggars.append(int(elements))
total_money = []
starting_index = 0

while starting_index < beggars:
    sum_of_money_for_beggar = 0
    for current_index in range(starting_index, len(numbers_money_for_beggars), beggars):
        sum_of_money_for_beggar += numbers_money_for_beggars[current_index]
    total_money.append(sum_of_money_for_beggar)
    starting_index += 1
print(total_money)