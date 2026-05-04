n=list(map(int,input("Enter Numbers :").split()))
for i in n:
    if i%2 == 0:
        print(i)

#using function
def even_num(num):
    for i in num:
        if i%2==0:
            print(i)
n=list(map(int,input().split()))
print(even_num(n))