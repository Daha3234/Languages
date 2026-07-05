#Sets

collection = {1, 2, 3, 4, 4, 4, "hello", "wprld"}
print(collection)
print(len(collection))

#emty set
collection1 = set()
print(type(collection1))

#method of set
#Add method

collection.add(1)
collection.add(2)
collection.add(2)



#Set remove(el)

#Set Clear method
collection.add(1)
collection.add(2)
collection.add("apnacollege")
collection.add((1, 2, 3,))

collection.clear()
print(len(collection))

#Set pop method
collection = {"hello" , "coding", "coding", "python"}
print(collection.pop())
print(collection.pop())

#Set union methon
set1 = {1,2,3}
set2 = {2,3,4}
print(set1.union(set2))
print(set1)
print(set2)

#Set intersection method

set1 = {1, 2, 3}
set2 = {1, 3, 5, 2}
print(set1.intersection(set2))
