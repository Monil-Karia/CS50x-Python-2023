# Debugging

Logical errors or Bugs in the program 

we want a output as  → height(4)

#
##

###

####

```python
def main():
    height = int(input("Height?: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * i)

if __name__ == "__main__":
    main()

#Output -> input(4)
#
##
###
```

We don't want the output which is written in here so how we can debug or solve this logical error in this program 

Approaches we can: 

1. We can print the value of i using print(i , end=” ”) → here we wanted to find that at what i we have our hashes ……….. Undo the change after analyzing 
2. Adding breakpoints in the code 

### breakpoints  - It  is **a very helpful addition to the python debugging feature**

At what line we want to pause or what part of the code we have to run for checking for the error we add the points from the VS code editor . 

- Debugging a Python code using breakpoints involves setting breakpoints in your code at specific points where you want to pause the execution and inspect the current state of variables, values, and objects.
- Once the debugger starts, it will stop at the first breakpoint, allowing you to inspect the current state of variables and other objects.

VS Code provides several debugging tools that can help you control the debugging process. Here are some of the most commonly used ones:

- Continue: This command resumes the execution of the code from the current breakpoint to the next breakpoint, or until the end of the program if there are no more breakpoints.
- Step Over: This command executes the current line of code and moves to the next line. If the current line of code is a function call, it will execute the entire function before moving to the next line.
- Step Into: This command executes the current line of code and moves to the next line, but if the current line of code is a function call, it will step into the function and pause at the first line of the function.
- Stop: This command stops the debugging process and returns to the editor.
- Restart: This command stops the debugging process and restarts it from the beginning.

### Watch this preferred video of Debugging in the VS Code for Python - https://youtu.be/KEdq7gC_RTA
