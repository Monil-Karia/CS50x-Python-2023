# Exceptions
Exceptions are something which are Human errors or Logical error in the program .

We should write our code such that error are handled successfully 

### Syntax Error

What could go wrong in this program ? (Curious Question)  

```python
x = int(input("What the X?: "))
print (f"x is {x}")

#What if we write some string in the Input value ? input - cat
#Error - Value Error: invalid literal for int() with the base 10: 'cat'
```

literals -  Raw data assigned to variables are literals 

### try & except used for error handling

- Errors which we have to handle while Coding
    1. ValueError → Python's ValueError **occurs when a function is called with the proper argument type but with the wrong value . Eg - Passing string where int is required.** 
    2. NameError → the NameError **occurs when you try to use a variable, function, or module that doesn't exist or wasn't used in a valid way**. 

```python
#code with try and expect
try:
	x = int(input("What the ?: "))
	print(f"x is {x}")
except ValueError:
	print("x is not an integer")
```

NameError is present in this code because the reason is when we return ‘cat’ as input in the int function the int return a value error means the x till now doesn’t know the value as ‘cat’ and hence as x didn’t get the value it shows the error as NameError as there was never a value of x in the program . 

```python

#More Understandable and minimal amount of work is done 
try:
	x = int(input("What the ?: "))
except ValueError:
	print("x is not an integer")

print(f"x is {x}")
#Error = NameError: name 'x' is not defined 
```

The best code we have written till now with all the erros are handled by the code →

```python
#Solving the same problem by using else keyword in the try and except 
try:
	x = int(input("What the ?: "))
except ValueError:
	print("x is not an integer")
else:
	print(f"x is {x}")
```

### pass - When we want to catch the error but essentailly we want to pass it

Here we are refering pass to ignoring the error , not wanted to print something , to do something with the error or just ignore it and moving forward.

### raise - The __raise__ statement allows the programmer to force a specified exception to occur.

Example Code → 

```python
raise NameError('HiThere')

#Output - NameError: HiThere
```
