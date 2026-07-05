#Nasted Dictionary
student = {
    "Ali": {
        "Age": 34,
        "Marks": 94.5
    },

    "Ahmed": {
        "Age": 78,
        "Marks": 34.8
    }
}
print(len(student))
print(list(student.keys()))

#Values method 

student = {
    "Ali": {
        "Age": 34,
        "Marks": 94.5
    },

    "Ahmed": {
        "Age": 78,
        "Marks": 34.8
    }
}
print(len(student))
print(list(student.values()))

#Items method
student = {
    "Ali": {
        "Age": 34,
        "Marks": 94.5
    },

    "Ahmed": {
        "Age": 78,
        "Marks": 34.8
    }
}
print(len(student))
print(student.items())

#Get method
#update(newDict) method

# print("Before") error hai
#print(student["name2"]) error hai
#print("After") bhi error ay ga
