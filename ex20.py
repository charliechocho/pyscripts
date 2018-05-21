from sys import argv

script, input_file = argv

def print_all(fileLines):
    print fileLines.read()

def rewind(fileStart):
    fileStart.seek(0)

def print_a_line(line_count, fileName):
    print line_count, fileName.readline(),

current_file = open(input_file)

print "First, let's print the whole file"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines."

current_line = 1
print_a_line(current_line, current_file)
print_a_line(current_line + 1, current_file)
print_a_line(current_line + 2, current_file)

current_file.close
