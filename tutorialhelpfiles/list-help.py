#useful list methods:
# you can also create a list using
#the list() constructor, use double brackets

list.append()
list.clear()
list.copy()
list.count()
list.extend()
list.index()
list.insert()
list.pop()
list.remove()
list.reverse()
list.sort()


#data type examples

list =['apple', 'banana', 'cherry']
print(list)
print(list[1])

for x in list:
    print(x)

if 'banana' in list:
    print('ya its in the list')

list.append('orange')
print(list)

list.insert(5, 'grape')
print(list)

list.remove('grape')
print(list)

#list.pop() removes the last item if not specified
#list.pop(0) will remove the indexed one
list.pop()
print(list)

#you can also do 'del list' to delete list entirely
del list[0]
print(list)

# list.clear() clears the list

#if you wanna copy the list
#you can't just do list2 = list
#because thats a reference, and anything that will
#happen to list will also happen to list2

list1 = list.copy()
print(list1)

#join two lists either by:
list3 = list + list1
#or:
for x in list1:
    list.append(x)
#or
list.extend(list2)
