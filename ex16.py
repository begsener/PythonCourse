<<<<<<< HEAD
#exercise 16
#close
#read
#readline
#truncate: empty the file
#write(stuff)

from sys import argv
script, filename = argv

print ("We're going to erase %r." % filename)
print ("If you don't want that, hit CTRL-C (^C).")
#stops
print ("If you do want that, hit RETURN.")
input ("?")
print ("Opening the file...")
target = open (filename, 'w')
#opens the file in writing mode
#r for read, a for append

print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I'm going to ask you for three lines.")
line1 = input ("line 1: ")
line2 = input ("line 2: ")
line3 = input ("line 3: ")

print ("I'm going to write these to the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ("And finally, we close it.")
target.close()
=======
#exercise 16
#close
#read
#readline
#truncate: empty the file
#write(stuff)

from sys import argv
script, filename = argv

print ("We're going to erase %r." % filename)
print ("If you don't want that, hit CTRL-C (^C).")
#stops
print ("If you do want that, hit RETURN.")
input ("?")
print ("Opening the file...")
target = open (filename, 'w')
#opens the file in writing mode
#r for read, a for append

print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I'm going to ask you for three lines.")
line1 = input ("line 1: ")
line2 = input ("line 2: ")
line3 = input ("line 3: ")

print ("I'm going to write these to the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ("And finally, we close it.")
target.close()
>>>>>>> c8bb34737bc484eb9350bc0efd6f8f17c3d673bd
