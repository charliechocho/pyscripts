import os


def createDir(exdir):
    print "Creating the %s folder!!" % directory
    os.mkdir(directory, 0755)
    print(os.listdir(os.getcwd()))

def delDir(remdir):
    print "Removing %s" % directory
    os.rmdir(directory)
    print(os.listdir(os.getcwd()))


directory = raw_input("Type Directory to create: ")

dirExist = os.path.isdir(directory)
if dirExist:
    delDir(directory)
else:
    createDir(directory)



print "That's all folks."
