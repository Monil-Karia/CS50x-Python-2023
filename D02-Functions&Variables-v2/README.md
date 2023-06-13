## Day 2 Functions and Variables

- int() - It is a not a type but a function in Python { int() }
    
    Interesting thing is when we treat input without specifying it treats as a string  
    
    ```python
    x = input("Write ur x?")  #1
    y = input("Write ur y?")  #2
    
    z = x + y #It should be 3 but....
    
    print(z)
    
    #Output - 12
    ```
    
    Bit of new Syntax { we are nesting the functions ,  as return value of inner function acts as a argument to outer function } 
    
    Ex :-
    
    ```python
    x = int(input("Write ur x? "))  # 3
    y = int(input("Write ur y? "))  # 4
    
    #Do we really need z variable 
    # z = int(x) + int(y)
    
    print(x + y) #Output - 7
    ```
    
- float()  - a number with a decimal points
    - Code Example
        
        ```python
        x = float(input("Write ur x? "))  
        y = float(input("Write ur y? "))
        
        print(round(x+y))
        ```
        
- round() - Documentation → round( number [ , ndigits ] )
    - Official documentation for the round Function -([https://docs.python.org/3.11/library/functions.html#round](https://docs.python.org/3.11/library/functions.html#round))
        
        <aside>
        💡 For the built-in types supporting `[round()](https://docs.python.org/3.11/library/functions.html#round)`, values are rounded to the closest multiple of 10 to the power minus *ndigits*; if two multiples are equally close, rounding is done toward the even choice (so, for example, both `round(0.5)`and `round(-0.5)`are `0`, and  `round(1.5)` is  `2`). Any integer value is valid for *ndigits*(positive, zero, or negative). The return value is an integer if *ndigits*is omitted or `None`. Otherwise, the return value has the same type as *number* .
        
        </aside>
        
        [ , ndigits ] → means that up to how many digits after decimal you have to round 
        

<aside>
💡 New thing to notice and Syntax is Weird some how but ya

Notice → we formated the string and combined with { z:, } for the   

```python
x = float(input("Write ur x? "))  #999
y = float(input("Write ur y? "))  #1

z = round(x + y)  #expected 1000

print(f"{z:,}")
#Output - 1,000
```

</aside>

<aside>
💡 Again we are playing with the fstring(formatted string) 
here we exceptionally defined the limit of the number after the decimal

```python
z1 = x / y          # 2 / 3 
										#expected -  0.666666666
print(f"{z:.2f}")   

#Output - 0.67
```

</aside>

## Our Own Functions

### def → Define the Function

Ex : 

```python
#Inundation is so important in python
hello(name):
    print(f"Hello {name}")

#Simple Program to take name and print it 
name = input("What is ur name? ")
hello(name)
```

We generally have a convection of the Python to define our main code in main() function and call it after the code Because of 2 reasons 

1. If we call an another function in the main() although wherever it is defined it gets runned successfully 
2. Its quite readable that a 3rd person can read from main()

Ex - 

```python
def main():            # Only here we have defined it not called it 
    name = input("What is your name ? ")
    hello(name)

def hello(name ="World.!"):    #here also we have defined it 
		print(f"Hello , {name}")  

main()  # Calling out the name function to run the program 
```

### Scope of Function or variable

```python
def main()
    name = input("What is your name ? ")
    hello()

def hello():
    print(f"Hello , {name}")  #here name is not in the scope of the hello function 

main()  # Calling out the name function to
```

### return - Keyword which returns the value

```python
#Example Syntax 
return (n ** 2)  # Here ** represents the Power of any on Left side 
```
