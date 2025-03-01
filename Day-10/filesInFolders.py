"""

TASK: Print a list of files under every folder provided by a user. 


Pseudocode: 

1. Take input of directories as a string 
2. Convert string into a list of directories
3. Iterate over the list of directories
4. For each directory, print the list of files in that directory
5. Handle errors and exceptions 

Why Exception handling? 

To prevent known runtime errors from causing premature program exit. 
Essentially, you tell the user how to correct an error in their inputs.  
The program can gracefully continue, instead of crashing with an unsightly error. 

Try--> code block that might cause an exception 
Except--> what type of exception? what to do when an exception occurs? 

"""

import os 

def main():
    folder_input=input("Enter the directories: ").split()

    for folder in folder_input:
        try: 
            print("______ Listing the files for folder: ", folder)
            list_of_files=os.listdir(folder)
            
            # we don't want to see a list object, we want to see a list of files on the screen. 
            #second loop to iterate through the list of files created by os.listdir() which creates a list object
            for file in list_of_files: 
                print(file)
            

        except PermissionError:
            print ("You don't have permission to list directory: ", folder)

        except FileNotFoundError:
            
            print("Please provide a valid directory.")
            break #use continue if you want to try the other inputs 
 
if __name__ == "__main__": 
     main()

