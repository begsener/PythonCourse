#exercise 18
#def creates a function
#dont finish the functions with end
#scripts with arguments
def print_two(*args):
    arg1, arg2 = args
    print ("arg1: %r, arg2: %r" % (arg1,arg2))

#we can do this
def print_two_again(arg1, arg2):
    print ("arg1: %r, arg2: %r" %(arg1,arg2))

#takes one arguments
def print_one(arg1):
    print ("arg1: %r" %arg1)

def print_none():
    print ("I got nothin'.")

print_two ("Beg", "Sen")
print_two_again ("Beg", "Sen")
print_one("beg")
print_none()
