price_coffee = 1.50
price_water = 1.00
price_coke = 1.40
price_snacks = 2.00


def calculation(product, quantity):
    if product == "coffee":
        return quantity * price_coffee
    elif product == "water":
        return quantity * price_water
    elif product == "coke":
        return quantity * price_coke
    elif product == "snacks":
        return quantity * price_snacks


product = input()
quantity = int(input())

print(f"{calculation(product,quantity):.2f}")