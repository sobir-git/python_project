#!/usr/bin/python

def get_negative_int():
    n = 1
    while(True):
        print("Enter a number: ")
        n = float(input())
        print("n is: " + str(n))
        if (n < 0):
            break
    return n;

x = get_negative_int()
print (str(x) + " is a negative number!")


