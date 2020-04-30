#tuples are ordered and unchangeable
# aka list = mutable
# tuple = immutable
# you can delete tuples entirely tho
# ie del tuple
# you can also join tuples
# tuple3 = tuple1 + tuple2
# use tuple() constructuer with
# double round brackets to make a tuple

#tuple methods:
.count()
.index()

x = ('apple', 'banana', 'cherry')
print(x[-1:3])

#you can convert tuple to list to change it
#and convert back to tuples

y = list(x)
y[1] = 'kiwi'
tuple = tuple(x)

for a in tuple:
    print(a)

print(type(x))
