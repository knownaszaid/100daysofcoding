"""Day 4 coding Statement:
Write a program to identify of the a number is positive or negative

Get an input number from the user and check whether it is a positive or negative number.

Input :
-10
0
15

Output :
Negative number
Neither positive nor negative
Positive number

"""

num = int(input("Enter any number: \n"))

if num < 0:
    print("Negative Number")
elif num ==0:
    print("Neither positive nor negative")
else:
    print("Positive Number")
    
