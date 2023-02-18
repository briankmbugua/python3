# SCRIPT
.py file this is what we call a script
# MODULE
A module is a .py script that contains one or more definations
# DEFINATIONS
Definations are functions that we define in a module that can be used by other scripts via the import keyword, The file name becomes the module name e.g if we have foo.py we would import that using import foo.Basic modules tend to work best when they are in the same directory as your main script

# IMPORT KEYWORD
For example import foo, python will load the script and bring all the definations into your current script
The functions are not imported directly into the script, but they are accessible via the module name.
 ```python

 # foo.py
 def bar():
    print('sorry we dont serve minors')

# TellBarjoke.py
import foo
foo.bar()
 ```
You can also inlude code that is not a function defination when importing a module.
It is only executed once when the module is first imported

 ```python
 # foo.py
 barJoke = 'sorry we dont serve minors')
 def bar():
    print(barJoke)

# TellBarjoke.py
import foo
foo.bar()
 ```
in most cases this is bad practice and shoulfd be avoided as it can create unintended side-effects

