def sort_tuple(tuple_list):
    return sorted(tuple_list,key=lambda x:x[1])
data=[(1,3), (2,1),(4,2)]
print(sort_tuple(data))