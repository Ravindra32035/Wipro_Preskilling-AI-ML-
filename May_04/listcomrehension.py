numbers=[1,2,3,4,5]

#List comprehension
squares=[x*x for x in numbers]
print(squares)

#List Comprehension with condition
even=[x for x in numbers if x%2==0]
print(even)

#List of strings
name=["rahul","ravi"]
upper_case=[name.upper() for name in name]
print(upper_case)

#List comprehension using functions.
def name_upp(name):
    name=[name.upper() for name in name]
    return name
name=["Ravi","Sai"]
print(name_upp(name))