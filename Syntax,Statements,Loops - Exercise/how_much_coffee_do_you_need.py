command = ""
coffee_counter = 0
while command != "END":
    command = input()
    if command.lower() == "coding" or command.lower() == "dog" or command.lower() == "cat" or command.lower() == "movie":
        if command.islower():
            coffee_counter += 1
        else:
            coffee_counter += 2
if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)