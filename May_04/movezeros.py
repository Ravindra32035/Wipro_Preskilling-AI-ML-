def move_zeros(nums):
    result=[x for x in nums if x!=0]
    zeros=[0]* (len(nums)-len(result))
    return result+zeros
n=list(map(int,input().split()))
print(move_zeros(n))