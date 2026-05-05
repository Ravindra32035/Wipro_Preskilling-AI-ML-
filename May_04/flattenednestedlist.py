def flatten(list):
    result = []
    for sublist in list:
        for i in sublist:
            result.append(i)
    return result
print(flatten([[1,2,3],[4,5,6],[7,8,9]]))