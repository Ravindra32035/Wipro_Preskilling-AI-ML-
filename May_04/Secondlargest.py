def list_num(nums):
    nums=list(set(nums))
    nums.sort()
    return nums[-2]
numbers=list(map(int,input().split()))
print("Second largest number is :",list_num(numbers))
