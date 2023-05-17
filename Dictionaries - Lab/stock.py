items = input().split()
products = input().split()
bakery = {}

for index in range(0, len(items), 2):
    key = items[index]
    value = items[index + 1]
    bakery[key] = int(value)
for product in products:
    if product in bakery.keys():
        quantity = bakery[product]
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
