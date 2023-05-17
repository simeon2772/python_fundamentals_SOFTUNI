iterations = int(input())
tank_capacity = 255
liters_in_tank = 0
for current_line in range(iterations):
    liters_of_water = int(input())
    if tank_capacity - liters_of_water < 0:
        print("Insufficient capacity!")
        continue
    tank_capacity -= liters_of_water
    liters_in_tank += liters_of_water
print(liters_in_tank)
