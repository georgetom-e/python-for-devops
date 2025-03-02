
"""
TASK: A user passes an AWS ec2_instance type (sml, med, lar) to this program as a command-line argument. 
You must print an appropriate message (that will cost 2 dollars, 4 dollars, 8 dollars a day) and also handle inavlid inputs. 

"""


import sys 

ec2_type=sys.argv[1]

if ec2_type=='sml':
    print("sml will cost 2 dollars/day.")
elif ec2_type=='med':
    print("med will cost you 4 dollars/day")
elif ec2_type=='lar':
    print("lar will cost you 8 dollars/day")
else:
    print("invalid ec2 type. Valid types are sml, med, lar")

