

#LIST and TUPLES 

#list is mutable, can be resized
names=[ 'something', 'else', 'this way', 'now']

print(names)

for i in names: 
    print (i)

names.append("comes")
names.remove("now")


print(names)

print(len(names))


#slicing lists: 

slice=names[0:3]  #IMP! the upper limit is exclusive! So this will include a list from 0th index element to 2nd index element. 
print(slice)


#sorting lists: 

print(names.sort())

#tuples are immutable, cannot be resized. 
#Because of this, the memory footprint and allocation of a tuple in better. 
names_tuple=('something', 'wicked', 'this way comes')
print(names_tuple)

