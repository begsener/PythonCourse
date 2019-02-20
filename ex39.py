#exercise 39
#learning about dictionaries

things = ['a', 'b', 'c', 'd']
print (things[1])

things[1] = 'z'
print (things[1])

print (things)
#you can only use numbers to get items out of a list.
#dictionary lets you use things other than numbers.

stuff = {'name': 'Zed', 'age': 36, 'height': 6*12+2}
print (stuff['name'])
print (stuff['age'])
print (stuff['height'])
stuff['city'] = "San Francisco"
print (stuff['city'])

stuff[1] = "Wow"
stuff[2] = "Neato"
print (stuff[1])
print (stuff[2])
print (stuff)

#del: deletes
del stuff['city']
del stuff[1]
del stuff[2]
print (stuff)

#create a mapping of state to abbreviation
states = ['Oregon': 'OR', 'Florida': 'FL', 'California': 'CA', 'New York': 'NY', 'Michigan': 'MI']
#create a basic set of statees and some cities in them
cities = ['CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville']

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
