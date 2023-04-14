## Some Important and Common Definations

Arguments  -  It is the input to the function that is somehow influence the behavior of an Function Eg: print(arguments)

Variable - It is a container for an value

= → Assigment Operator right to left 

pseudocode - Using normal language to express the thoughts methodically or algorithmically 

comments  - Note to yourself in the program 

Parameters  - What a function can take is a parameter (int size , int numbers ..etc), what we can pass in the function are parameters

## Types of Functions

- print()
    
     It is a Function to print on terminal \
    
    Documentation - *print(*objects , sep = ' ' , end = '\n' , file= sys.stdout , flush=False)*
    
    - *objects means that multiple objects can be passed
    - sep - Seprator ( When we pass the Arguments that is why when we passed 2 arguments we get seprated by single space)
    - end - it always gets redirected to next line when finished
    
    *When we have multiple Arguments to pass it automatically inserts space for you*
    
    ```python
    #ask user for thier name
    name = input("Whats your name? ")
    
    #Say hello to the User
    print("Hello, " + name)
    print("Hello, " , name)    #passing 2 Arguments
    #When we have multiple Arguments to pass it automatically inserts space for you
    
    #output - Hello, Monil
    #output - Hello,  Monil
    ```
    
- input()
    
     Function for the terminal to take input from user 
    
    ```python
    #Example Syntax
    #ask user for thier name
    name = input("Whats your name? ")
    ```
    
- split()
    
    For spliting the name or the argument of the function
    
    ```python
    #Example Syntax 
    first , middle, last = name.split(" ")
    #Say hello to the User
    print(f"Hello, {name}")
    print(f"My first name is {first}")
    print(f"My middle name is {middle}")
    print(f"My last name is {last}")
    ```
    
- strip()
    - Function used to remove the white spaces
        
        ```python
        #remove whitespace from Str
        name = name.strip()
        ```
        
    - contaradiction - It only removes the left and the right of the string not in between
    - we have lstrip() for left striping & rstrip() for right striping
- captilize()
    
    Function it used to capitalize the very first letter of the word 
    
    ```python
    #capitalize user's name
    name = name.capitalize()
    
    #input -       david      malan      
    #output David malan
    ```
    
- title()
    
    Function which is used to for capitlizing every first letter of word of occurance  
    
- 

## Code Examples and Et cetra

- Plus(+) sign is used to contcatinate the Strings
- Overriding the Pre Build Function

```python
print("Hello, " , end = '') #overridden
print(name)
print("hello ," , name , sep= "??") #Positional parameters
```

- Escaping means we are printing a quote in a Double Quotation marked parameter

```python
#Both Work as same 
print("hello , \"friend\"") #Escapeing 
print('Hello, "friend"')
```

- Format String(F string)  - It tells the Python that treat the String in a special way of string where we can pass arguments to it.

```python
#Syntax and example
print(f"Hello, {name}") 
```

- Input is case sensitive so it will take spaces and all in between stuff
- Combining the two or more function in the single line

```python
#remove whitespace from Str and capitalising the User's name using title
name = name.strip().title()
```

- One step forward

```python
name = input("Whats your name? ").strip().title()
```
