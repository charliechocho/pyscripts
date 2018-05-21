# -*- coding: utf-8 -*-

name = 'Mattias Söderberg'
age = 48
height = 180
weight = 90
eyes = 'blue'
teeth = 'white'
hair = 'blonde'
inch1 = 2.54
lbs1 = 2.204


print "Let's talk about %s" % name
print "He's %d years old" % age
print "He's %d cm long which is %d inches" % (height, height / inch1)
print "He weighs %d kilos, which is %d pounds" % (weight, weight * lbs1)

print "He's got %s eyes and %s hair" % (eyes, hair)

print "If I add %d, %d and %d I get %d" % (age, height, weight, age + height + weight)
