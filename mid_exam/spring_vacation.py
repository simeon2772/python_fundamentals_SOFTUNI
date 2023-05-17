days_vacation = int(input())
budget = float(input())
people_on_vacation = int(input())
fuel_per_kilometer = float(input())
food_per_person_day = float(input())
hotel_price_per_person = float(input())


total_price_food_hotel = days_vacation * ((people_on_vacation * food_per_person_day) + (people_on_vacation * hotel_price_per_person))
if people_on_vacation > 10:
    discount_price = total_price_food_hotel * 0.25
    total_price_food_hotel -= discount_price

total_expenses = 0
current_day_expenses = 0
for day in range(1, days_vacation + 1):
    current_day_traveled_distance = float(input())
    current_day_expenses += total_price_food_hotel + (current_day_traveled_distance * fuel_per_kilometer)
    total_expenses += current_day_expenses
    current_day_expenses -= total_price_food_hotel
    if day % 3 == 0 or day % 5 == 0:
        pass
    if day % 7 == 0:
        pass
