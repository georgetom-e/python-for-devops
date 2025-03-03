"""

Find common elements in two lists 

1. iterate through first list and check if every element is 'not in' list 2. 
2. append 'in' elements to a new answer list 


"""




def commonCheck(l1, l2): 
     
    ansList=[] 
    for element in l1: 
        if element in l2:
          ansList.append(element)
        else: 
           continue 
    return ansList


list1=[1,2,3,4,5]
list2=[2,23,1,6,7,8,9]


ans=commonCheck(list1, list2)

print(f"The common elements of {list1} and {list2} are: {ans}")


