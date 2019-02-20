<<<<<<< HEAD
#exercise 20
=======
#exercise 20
from sys import argv
script, input_file = argv

def print_all(f):
    print (f.read())
    #read and print the file

def rewind(f):
    f.seek(0)
    #goes to the first byte.

def print_a_line(line_count, f):
    print (line_count, f.readline())

current_file = open(input_file)
print ("First let's print the whole file:\n")
print_all(current_file)
print ("Now let's rewind, kind of like a tape.")
rewind(current_file)
print ("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
>>>>>>> c8bb34737bc484eb9350bc0efd6f8f17c3d673bd
