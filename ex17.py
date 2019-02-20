<<<<<<< HEAD
#exercise 17
from sys import argv
from os.path import exists

script, from_file, to_file = argv
print ("Copying from %s to %s" % (from_file, to_file))
#we could do these two on one line too.
in_file = open (from_file) #opens the source file
indata = in_file.read() #reads the source file
print ("The input file is %d bytes long" % len(indata))
print ("Does the output file exist? %r" % exists(to_file))
print ("Read, hit the RETURN to continue, CTRL-C to abort.")
input()
out_file = open(to_file, 'w')
#opens the target file in writing mode.
out_file.write(indata)
#writes the data
print ("Alright, all done.")

out_file.close()
in_file.close()
=======
#exercise 17
from sys import argv
from os.path import exists

script, from_file, to_file = argv
print ("Copying from %s to %s" % (from_file, to_file))
#we could do these two on one line too.
in_file = open (from_file) #opens the source file
indata = in_file.read() #reads the source file
print ("The input file is %d bytes long" % len(indata))
print ("Does the output file exist? %r" % exists(to_file))
print ("Read, hit the RETURN to continue, CTRL-C to abort.")
input()
out_file = open(to_file, 'w')
#opens the target file in writing mode.
out_file.write(indata)
#writes the data
print ("Alright, all done.")

out_file.close()
in_file.close()
>>>>>>> c8bb34737bc484eb9350bc0efd6f8f17c3d673bd
