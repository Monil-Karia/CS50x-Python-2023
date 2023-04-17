# Conditionals

**<=, >=, < , > , == , !=**

### To ask a question we have a Keyword → if

- Example Code →
    
    ```python
    x  = int(input("What is ur X? "))
    y  = int(input("What is ur Y? "))
    
    if(x<y):
        print("Y is Greater than X")    #inundation is V.V.Imp 
    if(x>y):
        print("X is Greater than Y")    #inundation is V.V.Imp 
    if( x == y):
        print("X is Equal to Y")
    ```
    

### Python Allows us to ask a question few more question  → elif

- Example Code →
    
    ```python
    x  = int(input("What is ur X? "))
    y  = int(input("What is ur Y? "))
    
    if(x<y):
        print("Y is Greater than X")    #inundation is V.V.Imp 
    elif(x>y):
        print("X is Greater than Y")    #inundation is V.V.Imp 
    elif(x == y):
        print("X is Equal to Y")
    ```
    
### Last keyword is → else

- Example Code →
    
    ```python
    if(x<y):
        print("Y is Greater than X")    #inundation is V.V.Imp 
    elif(x>y):
        print("X is Greater than Y")    #inundation is V.V.Imp 
    else:
        print("X is Equal to Y")       #Observe the Else Syntax in the code 
    ```
    

### Keyword **OR (used as -or- in program)**

- Example Code →
    
    ```python
    if x < y or x > y:         #or is in the small charaters 
        print("X is not equal to y")
    else:
        print("X is Equal to Y")
    ```
    

### Use of Arithmetic Operators we have - **%**

Basically it returns the remainder → 4 % 3 = 1 ,  4 % 5 = 4 … 

- Example Code
    
    ```python
    #use of Arithmetic Symbols use of % (MODULO)
    # we also used the functions to make this code more easy
    def main():
        number = int(input("Input: "))
        is_even(number)
    
    def is_even(X):
        if(X % 2 == 0):
            print("Number is Even")
        else:
            print("Number is Odd")
    
    main()
    ```
    

<aside>
💡 Some Mind Blowing code and their Syntax

```python
#use of Arithmetic Symbols use of % (MODULO)

def main():
    numberX = int(input("Input: "))
    is_even(numberX)
    numberY = int(input("Input: "))
    singleline_even(numberY)

def is_even(X):
    if(X % 2 == 0):
        print("Number is Even")
    else:
        print("Number is Odd")

def singleline_even(Y):
    return "Even" if Y % 2 == 0 else "ODD"

# def mindblowing(Z)
#     return (Z % 2 == 0)   # Returns TRUE and FALSE based on condition

main()
```

</aside>

### Keyword → match (it is like switch statements in the Programming languages)

```python
match name:
    case "Harry" | "Hermione" | "Ron":    #Read is clear and Program is precise 
        print("GriffinDor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
#Obseerve the sybtax of the Match and also how : is used every where 
# Again inundation is important in the Python be Careful .!
```
