#Dictionary
#It stores data in key value pairs.

student={
    "name":"Ravi",
    "Age":20,
    "Course":"python"
}
print(student)

print(student["name"])
print(student["Course"])

#Add a new key value pair
student["city"]="Bangalore"
print(student)

#update the data
student["Age"]=26
print(student)

#delete the data
del student["city"]
print(student)

#key iteration
for key in student:
    print(key)

#value iteration
for value in student.values():
    print(value)

# Loop through key value pairs
for key,value in student.items():
    print(key,value)

