# -*- coding: utf-8 -*-
print "clear\r"

name = raw_input('What\'s your name: ')
age = raw_input('How old\nare you?')
height = raw_input('How tall are you?\t')
weight = raw_input('How much do you weigh?')

print """Hello %s!!
So you´re %r years old, %r cm tall
and wheigh %r kilos.""" % (
name, age, height, weight)
