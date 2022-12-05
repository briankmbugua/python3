#to insert characters that are illegal in a string use escape
#characters
#an escape character is a backslash followed by the character you want to insert

txt = "We are the so-called \"vikings\" from the north"
"""
\. single quote
\\ backslash
\n newline
\r carriage return
\t tab
\b backspace
\f form feed
\ooo Octal value
\xhh Hex value
"""

print(txt)