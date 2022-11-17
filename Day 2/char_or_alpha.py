"""Description:
Take an input character from user and check whether it is an alphabet or not.

 

Input:
A
7

Output:
Not an alphabet
Alphabet

"""

char = input("Enter the Input:-\n")

if (char>="A" and char<="Z")or(char>="a" and char<="z"):
    print("Entered Input is Character")
else:
    print("Entered Input is not alphabet")
