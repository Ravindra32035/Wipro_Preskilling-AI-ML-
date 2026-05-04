numbers=[10,20,30,]
numbers.insert(1,99)#inserts number 99 at 2nd index
print(numbers)

numbers=[10,99,20,30,]
numbers.remove(99) #removes 99 number from list
print(numbers)

numbers=[10,20,30,]
numbers.pop()        # Removes the last number from the list.
print(numbers)

numbers=[10,20,30,]
print(len(numbers)) #prints the length of the list


numbers=[10,20,30,50,60]
print(numbers[1:4])