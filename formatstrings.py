#string slicing

a = "123456789"

print(a[2:5])#from index 2 to 5, index five not included
print(a[2:])#slicing to the end if last index not specified
print(a[-5:-2])#negative indexing start the slice from the end

print("MODIFY STRINGS")

b = "  Brian  "

print(b.upper())#uppercase
print(b.lower())#lowercase
print(b.strip())#remove white space from the beginning and the end

#replace strings
print(b.replace("B", "j"))#replace B with j
#split strings
c = ""