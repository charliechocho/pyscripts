import os

os.system('clear')


print "Let's practice everything."
print 'You\'d need to know \'bout escapees with \\ that do \n newlines and \t Tabs.'

poem = """
\tThe Lovely world
with logic so firmly planted
cannot discern\n the needs of Love
nor comprehend passion from intuition
and requeires an explanation
\n\t\twhere there is none.
"""

print "-" * 16
print poem
print "-" * 16

five = 10 - 2 + 3 - 6

print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of : %d" % start_point
print "We'd have %d beans, %d, jars and %d crates.\n" % (beans, jars, crates)

start_point = start_point / 10

print "We can also do it this way.\n"
print "We's have %d beans, %d jars and %d crates" % secret_formula(start_point)
