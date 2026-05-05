def find_missing(num):
    n=len(num)+1
    total=n*(n+1)//2
    return total-sum(num)
n=list(map(int,input().split()))
print(find_missing(n))