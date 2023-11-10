#Second statement
#import numpy
import numpy as np

#create a random list of integers
numbers = np.random.randint(1,15,10)
#print(numbers)

#create a new list for numbers<5
less_than_five = []

#for each number of the numbers list, add it to the new list if they are smaller than 5
for number in numbers:
    if number<5:
        less_than_five.append(number)

#print the new list
print(less_than_five)
