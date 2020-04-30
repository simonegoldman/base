#dictionaries are unordered, mutable/changeable
#and indexed
#use curly brackets
#dictionaries have keys, ie brand is a key
#dict constructor
# dict = dict(brand='ford, etc') <- uses = rather than
# colon when assigning

#dict methods
.clear()
.copy()
.fromkeys()
.get()
.items()
.keys()
.pop()
.popitem()
.setdefault()
.update()
.values()

dict = {'brand': 'ford', 'model':'mustang', 'year':'1964'}

#these two do the same thing
x = dict['model']
x = dict.get('model')
print(x)
print(dict)

#change a term by referring to its key name
dict['year'] = 2018
print(dict)

#loop thru a dictionary
#this returns the KEY names
for x in dict:
    print(x)
#to print values:
for x in dict.values():
    print(x)
#for both:
for x, y in dict.items():
    print(x,y)

#check if key exists
if 'model' in dict:
    print('yes')

print(len(dict))

# adding a new item to a dictionary
dict['colour'] = 'red'
print(dict)

#removing
dict.pop('model')
print(dict)

#NESTED dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)
