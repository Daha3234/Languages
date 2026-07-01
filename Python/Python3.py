#List and Tople 
# list Slicing  sublist

marks = [20, 34, 45, 67, 49]
print(marks[1:3])

marks = [20, 34, 45, 67, 49]
print(marks[1:])

marks = [20, 34, 45, 67, 49]
print(marks[-3:-5])



#List Methods
#list Append()

list = [1, 2, 3, 4]
list.append(10)
print(list)

# List Sort()
#Numbers
list = [1, 2, 3, 4]
list.append(10)
list.sort(reverse=True)
print(list)
 
#Values
list = ['a', 'b','d','c']
#list.append(10)
list.sort()
print(list) 

#List Reverse

list = ['a', 'b','d','c']
list.reverse()
print(list)


#List Insert()

list = [2, 1, 4]
list.insert(1, 5)
print(list)

#List Remove()

list = [2,3,3,5,6]
list.remove(3)
print(list)

#List Pop()

list = [2, 1, 3, 1]
list.pop(2)
print(list)


#Tuple Methods
#Tuple Index Method
tup = (1, 2, 3, 4,)
print(tup.index(2))


#Tuple count

tup = (1, 2, 3, 4, 2, 2)
print(tup.count(2))