#sets are unordered and unindexed

#set methods
set.add()
set.copy()
set.difference()
set.difference_update()
set.intersection()
set.intersection_update()
set.isdisjoint()
set.update()
set.issubset()
set.symmetric_difference()
set.symmetric_difference_update()
set.union()
#update inserts items in set2 to set 1
#ie set1.update(set2)
set.remove()
#if the item to remove doesn't exist
# it will raise an erorr
set.discard()
# if the item to discard doesn't exist
# it will not raise an error
set.pop()
set.clear()
# 'del set' deletes the whole set
#joining sets
set3 = set1.union(set2)
# # # both union() and update() will exclude dupes
# set constructor w double round brackets make a set



set = {'apple', 'banana', 'cherry'}

for x in set:
    print(x)
