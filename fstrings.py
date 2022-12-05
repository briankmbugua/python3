"""
strings in python are usually enclosed within double quotes("")
or single ('') to create an f string you only need to add an f or an F befor the 
opening quotes of your string

"This" is a string whereas f"This" is an f-String

PRINT VARIABLES USING PYTHON f-strings
{} specify the name of the variables inside a set of curly braces
SYNTAX
f"This is an f-string {var_name} and {var_name}."
"""

language = "Pyhthon"
school = "freecodecamp"
print(f"I'm learning {language} from {school}")

#expressions in f strings

num1 = 83
num2 = 9
print(f"The product of {num1} and {num2} is {num1 * num2}")
num = 87
print(f"Is num even? {True if num%2==0 else False}")

#methods in f-Strings

author = "jane smith"
print(f"This is a book by {author.title()}")

#functions inside python f-Strings

def choice(c):
    if(c%2 == 0):
        return "Learn python"
    else:
        return "Learn Javascript!"

print(f"Hello python, tell me what is should learn {choice(3)}")
print(f"Hello python, tell me what is should learn {choice(10)}")
