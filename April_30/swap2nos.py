#using arithemetic operator
n=int(input("Enter the value of n:"))
m=int(input("Enter the value of m:"))
n=n+m
m=n-m
n=n-m
print("After Swapping :")
print("n = ",n)
print("m = ",m)

#using third variable
n=int(input("Enter the value of n:"))
m=int(input("Enter the value of m:"))
temp=n
n=m
m=temp
print("After Swapping :")
print("n = ",n)
print("m = ",m)

#without third variable
n=int(input("Enter the value of n:"))
m=int(input("Enter the value of m:"))
n,m=m,n
print("After Swapping :")
print("n = ",n)
print("m = ",m)