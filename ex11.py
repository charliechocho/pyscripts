# -*- coding: utf-8 -*-

name = raw_input('What\'s your name: ')
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print """Hello %s!!
So you´re %r years old, %r cm tall
and wheigh %r kilos.""" % (
name, age, height, weight)
