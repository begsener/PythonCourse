#exercise 5
# " double quote means that it is a string

my_name = 'Zed A. Shaw'
my_age = 35
my_weight = 180 #lbs
my_height = 74
my_eyes = 'blue'
my_teeth = 'white'
my_hair = 'brown'

print ("Let's talk about %s." % my_name)  #%s means it is a string
print ("He's %d inches tall." % my_height) #%d means it is a number
print ("He's %d pounds heavy." % my_weight)
print ("Actually he is not too heavy.")
print ("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print ("His teeth are usually %s depending on the coffee." % my_teeth)
print ("If I add %d, %d and %d, I get %d. " %(my_age, my_height, my_weight, my_age + my_height + my_weight))

#%r means print this no matter what.
#rounding
#my_number=1.2344
#round(my_number)
