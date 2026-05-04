def max_num(numbers):
    return max(numbers)
input=list(map(int,input("Enter numbers :").split()))
print(max_num (input))

#using for loop
numbers=list(map(int,input().split()))
max_num=numbers[0]
for i in numbers:
    if i>max_num:
        max_num=i
print("Maximum Number in the list is", max_num)