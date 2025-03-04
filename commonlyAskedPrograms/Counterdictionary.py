
from collections import Counter

slist= ["george", "george", "coffee", "tea","coffee"]

#Convert list to a dictionary (keys=unique elements, values=count of those unique elements)
adict=Counter(slist)

#sort the dictionary
"""
dict.items() will return a list of tuples with key-value pairs
sorted() will sort by key 
dict() converts the list of tuples to a dictionary 


"""
sdict=dict(sorted(adict.items()))

#print
print("Sorted dictionary: ", sdict)