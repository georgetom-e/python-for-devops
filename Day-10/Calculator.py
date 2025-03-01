"""
Simple calculator with exception handling 

Don't forget to convert input to float/int!
Don't forget to print from the function!
"""

import sys

def add(a, b):
    print(a+b)
def sub(a, b): 
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b): 
    try:
        print(a/b)
    except ZeroDivisionError: 
        print("Invalid Divisor: Division by Zero")


n1=float(sys.argv[1])
op=sys.argv[2]
n2=float(sys.argv[3])

if op=="add": 
    add(n1, n2)
elif op=="sub": 
    sub(n1,n2)
elif op=="mul":
     mul(n1,n2)
elif op=="div":
    div(n1,n2)
else: 
    print("Invalid operation. Enter add, sub, mul, or div.")

