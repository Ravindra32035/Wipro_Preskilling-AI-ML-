def invert_dict(num):
    new_dict={}
    for key in num:
        new_dict[num[key]]=key
    return new_dict
print(invert_dict({"a":1}))