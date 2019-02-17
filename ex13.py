#exercise 13
from sys import argv
#import: adding features to the script
#argv: holds arguments

script, first, second, third = argv
#unpacks argv, rather than holding all the
#arguments, it gets assigned to four vars

print ("The script is called: ", script)
print ("Your first variable is: ", first)
print ("Your second variables is: ", second)
print ("Your third variable is: ", third)
