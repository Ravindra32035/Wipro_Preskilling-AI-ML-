def count_freq(nums):
    freq={}
    for i in nums:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq
numbers=input().split()
print(count_freq(numbers))