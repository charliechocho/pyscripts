# -*- coding: utf-8 -*-

from sys import argv

script, first = argv
print "The script is called: ", script
print "Wow, really %r " % first

Anything_more = raw_input('\tDo you like %r? ' % first)


#print "The second variable is: ", second
#print "The third variable is: ", third
#print "The third argument is: ", fourth
print "\t\t%s? Well alrighty then!!" % Anything_more
