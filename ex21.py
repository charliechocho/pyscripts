def add(a, b):
    print "Adding %d + %d." % (a, b)
    return a + b

def sub(a, b):
    print "Subtracting %d - %d" % (a, b)
    return a - b

def multi(a, b):
    print "Multiplying %d * %d." % (a, b)
    return a * b

def div(a, b):
    print "Dividing %d / %d." % (a, b)
    return a / b

print "Let's do some math functions!"

age = add(40, 8)
height = sub(200,20)
weight = multi(30, 3)
iq = div(120, 3)

print "Age: %d, Height: %d, Weight: %d, Iq: %d" % (age,
    height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, sub(height, multi(weight, div(iq, 2))))

print "That becomes : ", what, "Can you do it by hand?"
