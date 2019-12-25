#Dictionaries
#It is a collection of unordered,changeable & indexed & in {}.
#they have keys & values

thisdict={"brand":"Ford","Model":"Mustang","Year":1964}
print("my dictionary:",thisdict)

#acessing item
x=thisdict["Model"]
print("accessing:",x)

# setdefault()
ya=thisdict.setdefault("model","Bronco")
print("setdefault:",ya)

#using get()method for acessing item
y=thisdict.get("Model")
print("get:",y)

#change the values
thisdict["Year"]=2018
print("change value:",thisdict)

#using loop for print all keys name in dictionary 
for py in thisdict:
	print("for",py)

#using loop for print all values in dictionary 
for py in thisdict:
	print(thisdict[py])

# use the values() function to return values from dictionary
for yp in thisdict.values():
	print("value:",yp)

# use the keys() function to return values from dictionary
for yp in thisdict.keys():
	print("keys:",yp)

#loop through both keys ans values by using the item() function
for p,y in thisdict.items():
	print("items:",p,y)

# #formkeys()
# thisdict=dict.fromkeys(x,y)
# print("formkeys:",thisdict)

#adding items
thisdict["color"]="red"
print("addding:",thisdict)

#update
thisdict.update({"center":"vijaynagar"})
print("update:",thisdict)

#length
print("length:",len(thisdict))

# # removing the items using pop()function
# thisdict.pop("Model")
# print("pop:",thisdict)

## removing the items using popitem()function
thisdict.popitem()
print("popitem:",thisdict)

# #using del keyword
# del thisdict["brand"]
# print("del:",thisdict)
# ##or error
# #del thisdict
# # print(thisdict)

#copy a dictionary using built-in method copy()
mydict=thisdict.copy()
print("copy:",mydict)
#or copy a dictionary using built-in method dict()   
ppydict=dict(thisdict)
print("dict:",ppydict)

# using clear() method for empty the dictionary
thisdict.clear()
print("clear:",thisdict)

#check if exists or not 
if "Model" in thisdict:
    print("yes model is in it ") 
else:
	print("no model is not in it")
