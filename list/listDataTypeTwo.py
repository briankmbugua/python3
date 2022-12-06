#Append items
#to add an item to the end of the list use the append() method
thislist = ["apple", "banana", "cherry"]
print("before",thislist)
thislist.append("orange")
print("after", thislist)
#insert at a specific index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")#inser item at the second position
print(thislist)
#append elements from onether list to the current list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#you can also extend() using any iterable object

#remove() method removes the specified item
thislist.remove("banana")
#pop() method removes the specified index, if you don't specify index removes last item
thislist.pop(1)
#del keyword also removes the specified index
del thislist[0]
del thislist #remove list completely

thislist = ["apple", "banana", "cherry"]
thislist.clear()#emties the list the list remains but it has no content
print(thislist)