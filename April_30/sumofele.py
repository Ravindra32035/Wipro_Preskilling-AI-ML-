str=list(map(int,input("Enter Numbers :").split()))
total=0
for i in str:
    total+=i
print(total)

#using function
def list_sum(num):
    return sum(num)
numbers=list(map(int,input("Enter Numbers :").split()))
print(list_sum(numbers))