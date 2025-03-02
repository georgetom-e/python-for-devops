"""
LOOPS 

Use a 'for' loop when the number of iterations in known 
Use a 'while' loop when the number of iterations is unknown but depends on a condition 


FOR LOOP 

for variable in sequence  => for i in list/tuple/range()

remember that range(10) resolves to a list of numbers [0...9]


WHILE LOOP

itertaions dependent on the specified while condition 

"""

tpl=('something', 23, 'who?', 2343)

for i in tpl:
    print(i)

i=0 
while i <10: 
    print(i)
    i+=1

#use break to escape a loop when a condition is met
#use continue to skip an interation based on a condition, and continue iterating


#you are given a log file, use a for loop to print the lines with 'ERROR'

log_file = [
   "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed",
]

print("Analysing log file...")
for i in log_file: 
    if "ERROR" in i: 
        print(i)
print("Analysis complete.")