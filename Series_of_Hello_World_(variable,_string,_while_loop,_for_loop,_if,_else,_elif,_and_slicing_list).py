#Variable a & b

a = "Hello"
b = "World"

print(a, b)

print(a + " " + b)

#-----------
#Greeting

Greeting = "Hello"
Name = "World"
print(Greeting, Name)

#-----------
#while loop

counter = 0
while counter < 7:
    print(counter)
    counter = counter + 1
print("Hello World")

#-----------
#for loop

for i in range(2):
    print("Hello World")
    
#-----------
#list & for loop

mylist = ["Hello", "World"]
for i in mylist: 
    print("I say: ", i)
    
#-----------
#if, else & elif

import numpy as np
from numpy.random import randn

answer = None
x = randn()
if x > 1:
    answer = "Hello World more than 1"
elif x >= -1:
    answer = "Hello World Between -1 and 1"
else:
    answer = "Hello World less than -1"
print(x)
print(answer)

#-----------
#Slicing list
l1 = ["I", "Love", "You", "Hello", "World"]
l1[3:5]
