"""

TASK: List users who've created Pull Requets for the Kubernetes Project on GitHub. Also find the number of PRs for every user. 

Pseudocode: 

1. Use the requets module (for API calls)
2. Use the GitHub API call to find PRs for the repo 
3. Convert JSON response to a dictionary (Python can only understand its native data types)
4. List the PRs from the dictionary


"""

import requests

response=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

# print(response.status_code)

if response.status_code==200:

    res_dict=response.json()  #this line converts json into a list of dictionaries. 
#still, the entire dictionary is a big data-set, we need only the list of people who created the PRs.
    for element in range(len(res_dict)):
        print(res_dict[element]["user"]["login"]) #each subsequent index is a nested element: list element -> user key -> login key within user key 


else: 
    print("Sorry, can't connect to GitHub at the moment. Please check the network.")


