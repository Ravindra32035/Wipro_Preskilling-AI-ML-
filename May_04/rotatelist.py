def list_rotate(list,k):
    k=k%len(list)
    return list[-k:]+list[:-k]
print(list_rotate([1,2,3,4,5],2))