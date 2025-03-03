

"""

Check if a string is a palindrome 

1. reverse input string using list slicing [::-1] 
2. compare originial with reversed 

"""


def palCheck(test):
    if test==test[::-1]: 
        print(f"String {test} is a palindrome.")
    else: 
        print(f"String {test} is not a palindrome.")


in_str=input("Enter your test string: ")

palCheck(in_str)