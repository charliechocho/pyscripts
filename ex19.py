# -*- coding: utf-8 -*-

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just givet the function numbers directly:"
cheese_and_crackers(10, 20)

print "Or we can use variables:"
amount_of_cheese = int(raw_input("No# of Cheese: "))
amount_of_crackers = int(raw_input("No# of boxes: "))
print '\n'

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too: "
cheese_and_crackers(10 + 20, 5 + 6)

print "and we can combine the two: "
cheese_and_crackers(amount_of_cheese + 10, amount_of_crackers + 20)
