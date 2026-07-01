#Practice Questions
list = ()
list1 = input("Apple1: ")
list2 = input("Banna2: ")
list3 = input("Mango3: ")

list.append(list1)
list.append(list2)
list.append(list3)

print(list)

#Palindraw

list1 = [1, 2, 3, 2, 1]
list2 = [1, 2, 3,]

copy_list1 = list.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("Not palindrome")