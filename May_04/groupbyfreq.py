from unittest import result


def group_by_freq(nums):
    freq={}
    for i in nums:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    result={}
    for key in freq:
        count=freq[key]
        if count not in result:
            result[count]=[]
        result[count].append(key)
    return result
print(group_by_freq([1,1,3,3,3,6]))

