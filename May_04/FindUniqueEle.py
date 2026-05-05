def uniq_ele(list1,list2):
    return list(list1^list2)
a1=set(input().split())
a2=set(input().split())
print(uniq_ele(a1,a2))