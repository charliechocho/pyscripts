import os

print "I will now ask for some info!: "
answ = "yes"
while (answ == "yes"):
    firstName = raw_input('Enter First Name: ')
    lastName = raw_input('Enter Last Name: ')
    address = raw_input('Enter Street Address: ')

    inData = "%s\t%s\t%s\n" % (firstName, lastName, address)
    inData = inData.expandtabs(16)
    if inData:
        dataFile = open('db.txt', 'a+')
        dataFile.write(inData)
        dataFile.close()
    else:
        print "You didn't write anything"

    outData = open('db.txt').read()
    print outData
    answ = raw_input("Want to enter another one?(yes/no): ")
    os.system('clear')

print "Thanks for your input"
