"""
Booleans represnt one of two values: True or False
The bool() function allows yout to evaluate any value, and
give you True or False
"""
print(bool("Hello")) #true
print(bool(15)) #true

x = "Hello"
y = 15

print(bool(x)) #true
print(bool(y)) #true

"""
Almost all value are true if they have some content
Some values are false ie -- (), [], {}, "", the number 0, and 
the value None.And of course the value False evaluates to False.
"""

#the following will return false

print(bool(False),bool(None),bool(0),bool(""),bool(()),bool([]),bool({}))