def common_ele(list1,list2):
    s1=set(list1)
    s2=set(list2)
    if s1&s2:
        return "Yes"
    else:
        return "No"
n=list(input().split())
p=list(input().split())
print(common_ele(n,p))