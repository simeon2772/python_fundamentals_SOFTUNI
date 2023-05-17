budget = int(input())
command = input()

while command != "End":
    product_prize = int(command)
    budget -= product_prize
    if budget < 0:
        print("You went in overdraft!")
        break
    command = input()
else:
    print("You bought everything needed.")
