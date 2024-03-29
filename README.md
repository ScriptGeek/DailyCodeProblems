# DailyCodeProblems

This repo is for practicing code problems and learning the Python programming language.

## CHEAT SHEET


### STRINGS AND CHARACTERS

mystring = "Hello World"

ascii_code = ord(mystring[0])

H = chr(ascii_code)

### LIST

mylist = ["Hello", "World"]

mylist = map(func, list) # map - executes func on each item in list and returns new list

### DICTIONARY
mydict = { "Hello" : "World" } # dictionary ({:})


### SET
myset = { "Hello", "World" }

***Once a set is created its items cannot be changed, but items can be added or removed***

***Unindexable - data can only be accessed like this:***

**ACCESS SET ITEMS**

for x in myset:

  print(x)

**CHECK IF IN SET**

if ("Hello" in myset):

  print ("Hello is in the set!")

**ADD ITEMS**

myset.add("Wayne's World") # add one item

myset.update(["Party on, Dude", "Shwing"]) # add multiple items

**REMOVE ITEMS**

myset.remove("Shwing") #***if item does not exist an error will be raised***

myset.discard("Shwing") #***if item does not exist an error will NOT by raised***

x = myset.pop() #***will remove an item, but sets are unordered so it cannot be determined which one will be removed***

**EMPTY THE SET**

myset.clear()

**DELETE THE SET**

del myset

**JOIN 2 SETS**

set1 = {"a","b","c"}

set2 = {1,2,3}

set3 = set1.union(set2)

***or***

set1.update(set2) #**inserts all the items in set2 into set1**

**Constructor**

myset = set(("a","b","c")) #**note the double round brackets**


***COMPLETE SET OF METHODS:***

add() - Adds an element to the set

clear() - Removes all the elements from the set

copy() - Returns a copy of the set

difference() - Returns a set containing the difference between two or more sets

difference_update() - Removes the items in the set that are also not present in the other set

discard() - Removes the specified item

intersection() - Returns the set composing the intersection of two other sets

intersection_update() - Removes the items in the set that are not included in the other set(s)

isdisjoint() - Returns whether two sets have an intersection or not

issubset() - Returns whether another set contains this set or not

issuperset() - Returns whether this set contains another set or not

pop() - Removed an element from the set

remove() - Removes the specified element

symmetric_difference() - Returns a set with the symmetric differences of two sets

symmetric_difference_update() - Inserts the symmetric differences from this set and another

union() - Return a set containing the union of sets

update() - Update the set with the union of this set and others


### Tuple

mytuple = ("Hello", "World") # tuple ((,))

### Miscellaneous Functions

len: len(list), len(dictionary), len(string), len(

