#Generator
#Getting the data one at a time

def my_generator():
    yield 1
    yield 2
    yield 3
gen = my_generator()
for num in gen:
    print(num)