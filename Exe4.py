cars=100
space_in_a_car = 4.0
drivers = 30
passangers = 90
cars_not_driven = cars-drivers
cars_driven = drivers
carpool_capecity = cars_driven * space_in_a_car
average_passengers_per_car = passangers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capecity, "people today.")
print("We have", passangers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
"in each car.")
