#python doesn't need a main function; don't forget to invoke your custom function, if any.


def add(a,b):
    return a+b

def mul(a,b):
    return a*b

a=int(input("Enter your first number: "))
b=int(input("Enter your second number: "))

print("the sum of a and b is: ", add(a,b))
      
print("the product of a and b is: ", mul(a,b))


#Modules 


""" A python file with a group of useful functions can be re-used in other python programs. 

Group of Functions --> Module 

Suppose you have a python program with all mathematical functions defined: mathematics.py 
You can use that in a calculator.py as 

import mathematics as maths  (alias)

maths.add(a,b) (invoke the module and its function)

As a DevOps Engineer, you will create and re-use modules. 


PACKAGES / LIBRARIES 
A collection of modules 
Functions --> Modules --> Packages 

As a DevOps Engineer, you will mostly consume packages; won't create that many. 


The packages you will use (boto3, github, jira...) are created by smart people and pushed to PYPI (python packages index) analagous to Docker Hub. 
You will then install these packages for your use: 

pip install flask (for the flask framework)


How do I see packages already installed in my environment? 

pip list 


How do I prevent package version dependency conflicts?

Multiple projects with conflicting dependencies can be solved by using python virtual env (namespaces)
to logically separate packages for each project. 

pip install virtualenv

1. python -m venv someName  (create the virtual env namespace)

2. Activate the virtual environment (on Windows)
myenv\Scripts\activate

3. Activate the virtual environment (on macOS/Linux)
source myenv/bin/activate


"""


 




