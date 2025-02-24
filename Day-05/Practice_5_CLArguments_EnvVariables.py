"""
The sys module included in the default python installation helps you pass commandline arguments. 


"""

#you must import the sys package to use command-line arguments 
import sys 

#you must import the os module to read env variables
import os 

def add(a,b):
    return a+b

def mul(a,b):
    return a*b

def sub(a,b):
   return a-b

#sys.argv[0] holds the name of the script. 

#IMP: Don't forget to typecast python inputs to int/float! By default, inputs in python are in string
num1=float(sys.argv[1])
op=sys.argv[2]
num2=float(sys.argv[3])


if op=="add":
  print(add(num1, num2))
elif op=="mul":
   print(mul(num1,num2))
else:
   print(sub(num1, num2))

#Environment Variables

"""
Never hard code sensitive info like API-keys, certificates, passwords into a Python script. 
Use Environment Variables

export API_KEY="Dummy_12ae-#3452" (this creates a API_KEY env var on the system)

print(os.getenv("API_KEY")) in the program to print the env var

"""

print(os.getenv("API_KEY"))