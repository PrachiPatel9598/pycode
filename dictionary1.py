#dictionary

##create dictionary
dict1={'Name':'Prachi','Age':16,'Class':'Twelveth'}
print(dict1)
print("dict1['Name']:",dict1['Name'])
print("dict1['Age']:",dict1['Age'])
print("dict1['Class']:",dict1['Class'])
#print("dict1['Alice']:",dict1['Alice'])    // error 

##update dictionary
dict1['school']="TNGFPA"
print(dict1)

# #delete dictionary
# del dict1

#using clear to remove all entry
print("Start Len:%d" % len(dict1))
dict1.clear()
print("End Len:%d" % len(dict1))

# #remove entry with key "Name"
# del dict1['Name']

#length or dictionary
dict1={'Name':'Prachi','Age':16,'Class':'Twelveth'}
print("Length :%d" %len(dict1))

#using str() method
dict1={'Name':'Prachi','Age':16,'Class':'Twelveth'}
print("Equivalent String : %s" %str(dict1))

#using type() method
dict1={'Name':'Prachi','Age':16,'Class':'Twelveth'}
print("variable type: %s" % type(dict1))

#using copy()
dict1={'Name':'Prachi','Age':16,'Class':'Twelveth'}
dict2=dict1.copy()
print("New dictionary:",dict2)

#using fromkeys() method
seq=('Name','Class','Age')
dict=dict1.fromkeys(seq)
print("New Dictionary:%s" %str(dict1))
dict=dict1.fromkeys(seq,10)
print("New Dictionary:%s" %str(dict1))

#using get() returns a value for the given key
#dict.get(key, default=None)
dict1={'Name':'Yachi','Age':16,'Class':'Twelveth'}
print("Value:%s" %dict1.get('Age'))
print("Value:%s" %dict1.get('Class',"NA"))
print("Value:%s" %dict1.get('Ageee',"NA"))
print("Value:%s" %dict1.get('Ag'))

#using items() method
dict1={'Name':'Yachi','Age':16,'Class':'Twelveth'}
print("Values:%s" % dict1.items())
print(dict.items())

#using keys() method
dict1={'Name':'Yachi','Age':16,'Class':'Twelveth'}
print("Values:%s" % dict1.keys())

#using setdefault()method
#dict.setdefault(key, default=None)
dict1={'Name':'Yachi','Age':16,'Class':'Twelveth'}
print("Value:%s" %dict1.setdefault('Age',None))
print("Value:%s" %dict1.setdefault('Ageeee',None))
print(dict)

#2update() method 
dict1={'Name':'Yachi','Age':16,'Class':'Twelveth'}
dict3={"Nickname":'Prahi','Hobby':'Puzzles'}
print(dict1.update(dict3))

#using values()
dict1={'Name':'Yachi','Age':16,'Class':'Twelveth'}
print("Values:%s" % dict1.values())

