people = int(raw_input("How many people? "))
cats = int(raw_input("How many cats? "))
dogs = int(raw_input("How many dogs? "))


if people < cats:
    print "Too many cats, The world is doomed!!"

if people < (cats + dogs):
    print "Wow, lots of animals, few people!!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 10

if people >= dogs:
    print "People are greater than or equal to dogs!"

if people <= dogs:
    print "People are less than or equal to dogs!"

if people == dogs:
    print "People are dogs!"
