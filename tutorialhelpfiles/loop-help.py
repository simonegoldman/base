'''
#functions

#################### IF ####################
if:
elif:
else:
if a >b and a>c:
if a>b or a>c:
# you can also have nested if statements

# if statements cannot be empty,
# but if you for some reason have an if statement
# with no content, put in the pass statement to avoid
# getting an error.
if b<a:
    pass

'''
#################### WHILE LOOP ####################
# will execute a statement as long as the while
# condition is True
# break with break
# continue stops with the current iteration,
# and continues with the next
# else runs once the condition is no longer True

x = 1
while x <6:
    print(x)
    x +=1
else:
    print('x is no longer less than 6')


#################### FOR LOOP ####################
fruits= ['apple', 'banana', 'cherry']
for x in fruits:
        print(x)
        if x == 'banana':
            break

# loop thru letters in string
for x in 'abcdefg':
    print(x)

# range()
for x in range(5):
    print(x)

for x in range(2,30,5):
    print(x)
else: # this will print a message when the loop has ended
    print('done')

#nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# for loops cannot be empty, but if you
# for some reason have a for loop with
# no content, put in the pass statement
# to avoid getting an error

for x in [0, 1, 2]:
  pass
