def merg_dic(dic1,dic2):
    dic1.update(dic2)
    return dic1
dic1={"a":1,"b":2}
dic2={"c":1,"d":2}
print(merg_dic(dic1,dic2))