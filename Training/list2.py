from time import time


numbers = [i**2 for i in range(10)]

'''
numbers = list(map(lambda i: i**2 , range(10)))
********OR********
for i in range(10):
    numbers.append(i**2)
    '''

print(numbers)

#multiple the items in side the numbers list
times = [i*2 for i in numbers]
print(times)
#print greaterthan 50 numbers
print([i for i in times if i > 50 ])

