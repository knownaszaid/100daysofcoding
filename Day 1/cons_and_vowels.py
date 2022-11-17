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
"""

char= input("Enter the Character:-\n")

if (char=="a",char=="e",char=="i",char=="o",char=="u",char=="A",char=="E",char=="I",char=="O",char=="U"):
    print("Entered Character is vowel")
elif ((char>="A" and char<="Z")or(char>="a" and char<="z")):
    print("Entered Character is Consonant")
else:
    print("Input is Invalid")
