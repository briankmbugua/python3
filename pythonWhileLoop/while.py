"""Python has two primitive loop commands
1: while loops
2: for loops"""

"""with while loop we can execute a set of statements
as long as a condition is true"""

#print i as long as i is less than six

i = 1
while i < 6:
    print(i)
    i += 1#remember to increment i or else the loop will continue forever

#break statement
print("braek statement")
"""with break statement we can stop the loop even if
the while condition is true"""
i = 1
while i < 6:
  print(i)
  if i == 3:
    break#break if 1 equal 3 jump out of the loop
  i += 1

#the continue statement
"""with the continue statement we can stop the current iteration, and
continue with the next"""
print("the continue statement")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

print("the else statement")   
"""with the else statement we can run a block of
code when the condition is no longer true"""
i = 1
while i < 6:
    print(i)
    i += 1
else:
     print("i is no longer less than 6")   