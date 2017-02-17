#!/usr/bin/python
import sys

print("Please enter a number: ")
value= float(input())

x= 0

for x in range (0, 5):
    if (value < 0):
        print ("This value is negative")
    elif (value > 0):
        print("This value is positive")
    else:
        break
    x += 1
    print (value)