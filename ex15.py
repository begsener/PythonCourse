<<<<<<< HEAD
#exercise 15
from sys import argv
script, filename = argv
txt = open(filename)
print ("Here's your file %r: " %filename)
print (txt.read())

print ("Type the filename again:")
file_again = input ("> ")
txt_again = open (file_again)
print (txt_again.read())
=======
#exercise 15
from sys import argv
script, filename = argv
txt = open(filename)
print ("Here's your file %r: " %filename)
print (txt.read())

print ("Type the filename again:")
file_again = input ("> ")
txt_again = open (file_again)
print (txt_again.read())
>>>>>>> c8bb34737bc484eb9350bc0efd6f8f17c3d673bd
