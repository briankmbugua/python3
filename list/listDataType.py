"""
lists are used to store multiple items in a single variable
lists are created using square brackets
List items are ordered, changeable, and allow dupicate values
list items are indexed from [0] to [n]
ORDERED
list have a defined oreder
order will not change
if you add a new item to a list the item will be stored at the end of the list
some list methods can change order
CHANGEABLE
change,add,remove items in a list after it has been created
ALLOW DUPLICATES
Since lists are indexed, list can have items with the same value
DATATYPE
list items can be of any datatype, differnet data type
<class 'list'>
"""
thislist = ["apple", "banana", "cherry","cherry","banana",False,1,True]
print(thislist)
#LIST LENGHT
print(len(thislist))#dertermine how many items are in list
print(type(thislist))#<class 'list'>
#you can use the list constructor to create a new list
#list()
thislist = list(("brian","kinyanjui","mbugua","oscar","njenga"))
print(thislist)
#ACCES
print(thislist[1])
print(thislist[-1])#negative indexing means start from the end
#RANGE OF INDEXES
"""
you can specify the range where to start and where to end
the range
when specifying a range, the return value will be a new list
with specified items
"""
#return the third, fourth, and fifth item
print(thislist[2:5])#start from index two not inclusive of the last index
print(thislist[-5:-2])
#check if item exists
if "brian" in thislist:
    print("Yes, 'brian' is in thislist")

#change list items
thislist[1] = "blackcurrant"

print(thislist)

#cHANNGE A RANGE OF ITEMS
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

newlist = ["apple", "banana", "cherry"]
print(newlist)
newlist[1:2] = ["blackcurrant", "watermelon"]
print(newlist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#to inser items without replacing any of the existing value use insert() method
#inser "watermelon" as the third item

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)#as a result the list now contains four items