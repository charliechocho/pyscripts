# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

#print "Truncating the file! Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line1: ")
line2 = raw_input("Line2: ")
line3 = raw_input("Line3: ")

lines_of_text = "%s%s%s" % (line1, line2, line3)
print lines_of_text
target.write(lines_of_text)
print "And finally we close it!!"
target.close()
