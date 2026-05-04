n=input("enter a string :-").lower()
count=0
for ch in n:
    if ch in "aeiou":
        count+=1
print(count)

#using function
def count_vowels(text):
    return sum(1 for ch in text.lower() if ch in "aeiou")
text=input("enter a string :-")
print(count_vowels(text))