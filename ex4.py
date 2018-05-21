# Variables and calculations

cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars * space_in_car
available_carpool_capacity = drivers * space_in_car
average_passenger = passengers / cars_driven
optimal_car_use = passengers / space_in_car


print "There are ", cars, "cars available."
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "cars not running today"
print "We can drive", available_carpool_capacity, "people today"
print "We have", passengers, "to carpool today"
print "We need to put", average_passenger, "in each car."
print "Or we could use ", optimal_car_use, "cars instead to be more green"
