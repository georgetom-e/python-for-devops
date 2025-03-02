"""
The sys module included in the default python installation helps you pass commandline arguments. 


"""


import sys 

fname=sys.argv[0]
lname=sys.argv[1]

print("Your full name is", fname, lname)