#when ever if the data didn"t want to be tampered we use tuple
#tuple and list are both same only with one change from tuple side it is immutable.

numbers =(1,2,3,4,5)
print(numbers[0])
print(numbers[1])

print(numbers[-1])


print(numbers[1:4])

# number[1]=99 #this thing only will not work in tuple

def tuple_print(n):
    return n[::-1]
m=tuple(int(input().split()))
print(m)