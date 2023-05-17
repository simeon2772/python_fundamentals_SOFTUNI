my_dict = {}
while True:
    products = input().split(': ')
    if products[0] == "statistics":
        print(f"Products in stock:")
        for product, quantity in my_dict.items():
            print(f"{product}: {quantity}")
        print(f"Total Products: {len(my_dict)}")
        print(f"Total Quantity: {sum(my_dict.values())}")
        break

    key, value = products
    if key not in my_dict.keys():
        my_dict[key] = 0
    my_dict[key] += int(value)