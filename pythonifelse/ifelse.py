"""
IDENTATION
python relies on identation(whitespace at the beginning of a line)
to define scope
"""
#if statement

a = 33
b = 200
if b > a:
    print("b is greator than a")

#Elif if the previous coditions were not true, then try this condition

a = 33
b = 33
if b > a:
    print("b is greator than a")
elif a == b:
    print("a and b are equal")

#else catches anything which isn't caught by the preceding conditions
a = 33
b = 33
if b > a:
    print("b is greator than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greator than b")    

#you canhave else without elif:
a = 200
b = 33
if b > a:
    print("b is greator than a")
else:
    print("b is not greator than a")

#short Hand if
if a > b: print("a is grator than b")
#short hand if... Else
"""if you have one statement to execute
one for if and one for else you can put it all on the same line
this technique is known as Ternary Operators, or Conditional Expressions"""
a = 2
b = 300
print("A") if a > b else print("B")
"""you can also have multiple else statements on the same line"""
a = 300
b = 330
print("A") if a > b else print("=") if a == b else print("B")
#AND
"""the and keyword is a logical operator and is used to combine conditional statements"""
a = 200
b = 33
c = 500
if a > b and c > a:
    print("both conditons are true")
#Or
"""The or keyword is a logical operator, and is used to combine conditional statements"""
a = 200
b = 33
c = 500
if a > b and c > a:
    print("at least one of the conditions is true")
#nested if
"""if you have if statements inside if statements this is called nested if statements"""

x = 41

if x > 10:
    print("Above ten")
    if x > 20:
        print("Also above ten")
    else:
        print("But not above 20")
#the pass statement
a = 33
b = 200
if b > a:
    pass          