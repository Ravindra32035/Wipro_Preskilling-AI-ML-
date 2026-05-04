def fibb_series(a):
    return a == a[::-1]
n=input("Enter a Word: ")
if fibb_series(n):
    print("IS PALINDROME")
else:
    print("IS NOT PALINDROME")
