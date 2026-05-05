def first_non_repeat(num):
    freq={}
    for i in num:
        if i  in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for i in num:
        if freq[i]==1:
            return i
print(first_non_repeat([1,2,3,4,1]))