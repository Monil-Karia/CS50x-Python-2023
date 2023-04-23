# Libraries 
Share codes with other , share codes with ourself python have created the library

Library has build in functions or modules or  features 

Purpose of module or library is increase the reusability of the code . 

Libraries we get with python :- 

1. random - One or more function in order to do things randomly
    
    [docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html)
    
    - Example Code(choice) →
        
        ```python
        random.choice(seq)
        
        #Here we called the random lib and also a built in functon of choice 
        #seq here is type of list or any list in the program
        ```
        
    - Example Code (randint(a,b))→
        
        randint(a,b) → here we using any random int number between a and b 
        
        ```python
        import random
        
        number = random.randint(1,10)
        print(number) 
        ```
        
    - Example Code(shuffle(x)) →
        
        It shuffles the x where x is list , it dosen’t return anything it just shuffles the list in its place only 
        
        ```python
        import random 
        
        cards = ["Jack" , "Queen" , "king"]
        
        random.shuffle(cards)
        
        print cards
        ```
        
2. statistics - This module provides functions for calculating mathematical statistics of numeric data.
    
    [docs.python.org/3/library/statistics.html](https://docs.python.org/3/library/statistics.html)
    
    - Example Code(mean) →
        
        mean -mean between numbers or avg. of numbers 
        
        ```python
        import statistics
        
        #Returns mean of the twi numbers 
        print(statistics.mean([100 ,90 ]))
        ```
        
3. sys → 
    - command-line arguments → sys is module where we take input from user on command line
        - sys.argv[ ] → argv stands for argument vector , we take input from user in cmd line
            
            ```python
            import sys
            
            #here 1 in sys.argv because sys.argv [0] has name of file we are interpreting   
            print("Hello my name is", sys.argv[1])
            
            #cmd line input -> python name.py Monil
            #cmd line output -> Hello my name is Monil
            ```
            
        - sys.exit() → It will exit the program as it will improve the error handling of the program
            
            ```python
            ##New concept 
            #here 1 in sys.argv because sys.argv [0] has name of file we are interpreting   
            
            #Check for errors
            if len(sys.argv) < 2:
                sys.exit("Too few Arguments")
            elif len(sys.argv) > 2:
                sys.exit("Too many Arguments")
            
            #Priting the name  
            print("Hello , my Name is :" , sys.argv[1])
            ```
            
        
        **IndexError: list index out of range (when we not give arguments in cmd )**
        
- We use **import** keyword to take use of library in our code that’s why we have to write random.choice , random.func
    - We are able to increase the readability of the program  where will know that the choice function is extracted from random library
- We use **from**  we import some specific functions of the library that’s why we have to just write choice ,  function
    - This can provide a advantage in length of code writing continuously same code again and again it will increase the length and can look clumsy
- We have a **slice** where we take only the subset of the list to use it .
    
    ```python
    import sys
    
    if len(sys.argv) < 2:
        sys.exit("Too few Arguments")
    
    for arg in sys.argv[1:]:
        print("Hello , my name is ", arg)
    
    #if we use the sys[1:-1] then -1 reprsents that it is taking the index from behind 
    # -1 represents that it will not take last element from the list and will not print 
    # the last element from the arg which we have passed in the cmd
    ```
    

### Packages → It is a 3rd party lib that we can install in our PC to gain more functionality

pip → It is a package manager for Python

 PyPI ([pypi.org](http://pypi.org/)) → repository for the Python packages as pip is manager and retrieve from pypi 

Package Example - cowsay → Printing cow, trex or dragon saying our name as argument passed to it  

### API’s → Application programming Interface

**requests** → It is library that requests **URL(HTTP)**  from the browser and use it our program 

**Requests** is a simple, yet elegant, HTTP library.

site → [https://pypi.org/project/requests/](https://pypi.org/project/requests/)

```python
# https://itunes.apple.com/search7entity=song&limit=1&term=weezer -API by Apple's 

import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

#Pytohn code that pretend to be web browser

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

# print(json.dumps(response.json() , indent=2)) #Prints content of the reposne

res_ = response.json()
 
#We are just concern with trackname in the list of result 
for result in res_["results"]:
    print(result["trackName"])
```

### Creating our own library →

we have to just create the sayings.py and  call it in callSayings.py using 

“from sayings import hello” which helps us to import hello function from the file 

```python
def main():
    hello("World")
    goodbye("World")

def hello(name):
    print(f"Hello , {name}")

def goodbye(name):
    print(f"GoodBye, {name}")

## Important -> Here we written if statement instead of calling of main()
# because whenever we will call this outside the program or import it 
# main() will cause it to run main first then other program where as this one will be 
# more handy as well as 
if __name__ == "__main__":
    main()
```

 In this below program we called the sayings.py and we made improvements that if __name__ == "__main__" then it will only call main when required

```python
# callSaying.py
import sys
from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
```

**When a Python script is run directly, using the command `python sayings.py`, the `__name__`variable is set to `'__main__`. This allows the script to detect if it is being run as the main program or if it is being imported as a module into another program.**

### Refer my Notion link for better understanding and more readability of the theory → [https://jagged-fighter-969.notion.site/Libraries-3d51c6ba92ae47789e66d4c82a87fcf9](https://www.notion.so/Libraries-3d51c6ba92ae47789e66d4c82a87fcf9)
