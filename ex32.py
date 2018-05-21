count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

def in_a_row(getIt):
    rowUp = ""
    for number in getIt:
        rowUp = rowUp + "%s " % number
    print rowUp
# this first kind of for-loop goes through a list
print "Numbers from list in a row:"
in_a_row(count)

# same as above
print "Fruits in a row: "
in_a_row(fruits)

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it

for i in change:
    print "I got %s" % str(i)

# we can also build lists, first start with an empty one

elements = []

# then use the range function to do 0 to 5 counts

for i in range(0, 11):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
listFile = open("elements.txt", 'a')

for i in elements:
    print "Element was: %d" % i
listFile.write(str(elements))
listFile.write("\n")
listFile.close()
