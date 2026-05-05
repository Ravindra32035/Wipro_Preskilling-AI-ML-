#Brute Force Algorithm
def find_max(arr):
    max_num=arr[0]
    for i in arr:
        if i>max_num:
            max_num=i
    return max_num
print(find_max([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))