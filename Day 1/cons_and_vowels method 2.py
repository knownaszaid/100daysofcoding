"""Description
Take an input character from the user and check whether the given input is vowel or consonant.
Input
A
m
3
Output
Vowel
Consonant
Invalid input


-------------------------------Method 2------------------------------------
"""

char= input("Enter the Character:-\n")

if (char.lower() in('a','e','i','o','u'))or(char.upper() in('A','E','I','O','U')):
    print("Entered Character is vowel")
elif ((char>="A" and char<="Z")or(char>="a" and char<="z")):
    print("Entered Character is Consonant")
else:
    print("Input is Invalid")
