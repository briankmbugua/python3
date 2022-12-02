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
c = "Hello, world"
print(c.split(","))#return ['Hello', ' world']
#string concantation
first = "brian"
second = "mbugua"
fullname = first + second
print(fullname)#string concantation
age = 36
txt = "my name is and am {}"
print(txt.format(age))#age will be the placeholders are i.e {}
#yiu can use index numbers {0} to be sure the arguments are placed in the 
#correct placeholders
quantity = 3 #0
itemno = 567 #1
price = 49.95 #2
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
