def min_coins(amount):
    coin=[10,5,2,1]
    count=0
    for i in coin:
        while amount>=i:
            amount-=i
            count+=1
    return count
print(min_coins(6))