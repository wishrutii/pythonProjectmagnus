s1 = {10,30,40,23,76,'hello'}
print(type(s1)) # set is identified by {}, also it's mutable but has restrictions.
print(s1) # set is an unordered collection, so index positions don't work as it's not a concept available for set
# collection.
s1.add(100) # append can't be used, use add as this as a mutable collection but with restrictions.
print(s1) # it will add it randomly to any position.
s1.remove(23) # remove function can be used.
print(s1)

