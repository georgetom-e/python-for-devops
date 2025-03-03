"""

TASK: Update a server.config file and update a specific value with a provided value. 

1. Open file in Read mode 
2. Store file contents into a variable 
3. Open file in Write mode 
4. Update only the required line 


"""

def update_file(filepath, key, value):

    with open(filepath, 'r') as file: #rename filepath as file
        lines=file.readlines()   #copies file contents into lines 

    with open(filepath, "w" ) as file: 
        for i in lines: 
            if key in lines: 
               file.write(key + "=" +value + "\n")
            else: 
                file.write(lines)  #overwrite with the same data; same as continue


update_file("server.conf" "MAX_CONNECTIONS", "1000")


 



