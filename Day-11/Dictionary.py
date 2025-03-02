

#for a dictinary, define the keys as strings, and values as their respective types. 
#print an entire dict by printing its name, reference a specific key's value, by calling they key name as an index. 

first_dictionary={

  "name": "george", 
  "age": 100,
  "job": "devops",
  "AQN": 3.14,

}

print(first_dictionary)
print(first_dictionary["age"])


#A common use case is a list of dictionaries 

ec2_list=[

 {"name": "i2" , #don't forget the commas!
  "type": "t2.micro"},

 {"name": "i2" ,
  "type": "t2.medium"},

   {"name": "i3", 
  "type": "t2.xlarge"}

]

#Note the access format: ec2_list[1]["type"] --> first access the list element (a dictionary) --> then access the required key. 

print(ec2_list[1]["name"])
print(ec2_list[2]["type"])