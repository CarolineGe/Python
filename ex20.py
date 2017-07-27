from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)  #back to the origin

def print_a_line(line_count,f):
    print line_count, f.readline(), #f.readline comes with a \n on its own, to avoid the skip line, add a comma

current_file = open(input_file) #open first and then can be assigned to a file variable

print "first let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
