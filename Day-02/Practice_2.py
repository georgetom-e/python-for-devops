test="  george/tom"
print("test string is ", test)

#.split() splits the string on the basis of the character passed
# split results stored in an array; access elements using array indices  
split=test.split("/")
print("the zeroth split element", split[0])
print("the first split element", split[1])


#.strip() removes trailing/leading whitespaces /particular char from the string 
test2="  george is my name"
strip=test2.strip()
print("The stripped string:", strip)

#convert to upper/lower
upper=test.upper()
lower=test.lower()
print("string in upper", upper)
print("string in lower", lower) 

##find the length of a string 
length=len(test)
print("The length of the string: ", length)

#find if a substring exists in a string
sub='geo'
if sub in test: 
    print (sub, "is in", test )
else: 
    print (sub, "is not in", test)





