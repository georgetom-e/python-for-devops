"""Regular expressions (regex or regexp) are a powerful tool for pattern matching and text processing.
The re module in Python is used for working with regular expressions.
Common metacharacters: . (any character), * (zero or more), + (one or more), ? (zero or one), [] (character class), | (OR), ^ (start of a line), $ (end of a line), etc.
Examples of regex usage: matching emails, phone numbers, or extracting data from text.
re module functions include re.match(), re.search(), re.findall(), and re.sub() for pattern matching and replacement."""



import re 

text="python is a great tool."


#how to search for a pattern:
#  re.search() checks everywhere 
#  re.match() only checks the beginning of a string 

pattern=r"great"

#returns a Bool value 
search=re.search(pattern, text)
match=re.match(pattern, text) #won't find 


if search:
    print("pattern found:", search.group())
else: 
    print(pattern, "not found")

if match:
    print("match found", match.group())
else: 
    print("match not found")

#search and replace 

replacement="bad"

new_str=re.sub(pattern, replacement, text)
print("new string: ", new_str)

#split 
langs= "python,golang,rust,java,C++"
splitBy=","
result=re.split(splitBy, langs)
print("original string: ", langs)
print("regex splitby result", result)