# Et-Cetra 
- Over the many past lessons, we have covered so much related to Python!
- In this lesson, we will be focusing upon many of the “et cetera” items not previously discussed. “Et cetera” literally means “and the rest”!
- Indeed, if you look at the Python documentation, you will find quite “the rest” of other features.

## **`[set](https://cs50.harvard.edu/python/2022/notes/9/#set)`**

- In math, a set would be considered a set of numbers without any duplicates.

In the text editor window, code as follows:

```python
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = []
**for** student **in** students:
    **if** student["house"] **not** **in** houses:
        houses.append(student["house"])

**for** house **in** sorted(houses):
    print(house)
```

Notice how we have a list of dictionaries, each being a student. An empty list called `houses` is created. We iterate through each `student` in `students`. If a student’s `house` is not in `houses`, we append to our list of `houses`.

- It turns out we can use the built-in `set` features to eliminate duplicates.

In the text editor window, code as follows:

- Code Example
    
    ```python
    students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"},
        {"name": "Padma", "house": "Ravenclaw"},
    ]
    
    houses = set()
    **for** student **in** students:
        houses.add(student["house"])
    
    **for** house **in** sorted(houses):
        print(house)
    ```
    

Notice how no checking needs to be included to ensure there are no duplicates. The `set` object takes care of this for us automatically.

- You can learn more in Python’s documentation of `[set](https://docs.python.org/3/library/stdtypes.html#set)`.

## **[Global Variables](https://cs50.harvard.edu/python/2022/notes/9/#global-variables)**

- In other programming languages, there is the notion of global variables that are accessible to any function.

Notice how we create a global variable called `balance`, outside of any function.

Notice how we now add the functionality to add and withdraw funds to and from `balance`. However, executing this code, we are presented with an error! We see an error called `UnboundLocalError`. You might be able to guess that, at least in the way we’ve currently coded `balance` and our `deposit` and `withdraw` functions, we can’t reassign it a value value inside a function.

To interact with a global variable inside a function, the solution is to use the `global` keyword. In the text editor window, code as follows:

Notice how the `global` keyword tells each function that `balance` does not refer to a local variable: instead, it refers to the global variable we originally placed at the top of our code. Now, our code functions!

Utilizing our powers from our experience with object-oriented programming, we can modify our code to use a class instead of a global variable. In the text editor window, code as follows:

- Code Example
    
    ```python
    **class** **Account**:
        **def** __init__(self):
            self._balance = 0
    
        @property
        **def** balance(self):
            **return** self._balance
    
        **def** deposit(self, n):
            self._balance += n
    
        **def** withdraw(self, n):
            self._balance -= n
    
    **def** main():
        account = **Account**()
        print("Balance:", account.balance)
        account.deposit(100)
        account.withdraw(50)
        print("Balance:", account.balance)
    
    **if** __name__ == "__main__":
        main()
    ```
    

Notice how we use `account = Account()` to create an account. Classes allow us to solve this issue of needing a global variable more cleanly because these instance variables are accessible to all the methods of this class utilizing `self`.

- Generally speaking, global variables should be used quite sparingly, if at all!

## **[Constants](https://cs50.harvard.edu/python/2022/notes/9/#constants)**

- Some languages allow you to create variables that are unchangeable, called “constants”. Constants allow one to program defensively and reduce the opportunities for important values to be altered.

Notice `MEOWS` is our constant in this case. Constants are typically denoted by capital variable names and are placed at the top of our code. Though this *looks* like a constant, in reality, Python actually has no mechanism to prevent us from changing that value within our code! Instead, you’re on the honor system: if a variable name is written in all caps, just don’t change it!

Because `MEOWS` is defined outside of any particular class method, all of them have access to that value via `Cat.MEOWS`.

## **[Type Hints](https://cs50.harvard.edu/python/2022/notes/9/#type-hints)**

- In other programming languages, one expresses explicitly what variable type you want to use.
- As we saw earlier in the course, Python does require the explicit declaration of types.
- Nevertheless, it’s good practice need to ensure all of your variables are of the right type.
- `mypy` is a program that can help you test to make sure all your variables are of the right type.
- You can install `mypy` by executing in your terminal window: `pip install mypy`.
- that `number = input("Number: )"` returns a `string`, not an `int`. But `meow` will likely want an `int`!

Notice, though, that our program still throws an error.

- After installing `mypy`, execute `mypy meows.py` in the terminal window. `mypy` will provide some guidance about how to fix this error.

Notice how running `mypy` how produces no errors because cast our input as an integer.

Notice how the `meow` function has only a side effect. Because we only attempt to print “meow”, not return a value, an error is thrown when we try to store the return value of `meow` in `meows`.

Notice how the notation `-> None` tells `mypy` that there is no return value.

We can modify our code to return a string if we wish:

- Code Example
    
    ```python
    **def** meow(n: int) -> str:
        **return** "meow**\n**" * n
    
    number: int = int(input("Number: "))
    meows: str = meow(number)
    print(meows, end="")
    ```
    

Notice how we store in `meows` multiple `str`s. Running `mypy` produces no errors.

- You can learn more in Python’s documentation of [Type Hints](https://docs.python.org/3/library/typing.html).
- You can learn more about `[mypy](https://mypy.readthedocs.io/)` through the program’s own documentation.

## **[Docstrings](https://cs50.harvard.edu/python/2022/notes/9/#docstrings)**

A standard way of commenting your function’s purpose is to use a docstring. In the text editor window, code as follows:

- You can use docstrings to standardize how you document the features of a function. In the text editor window, code as follows: s
    - Code Example
        
        ```python
        **def** meow(n):
            """
            Meow n times.
        
            :param n: Number of times to meow
            :type n: int
            :raise TypeError: If n is not an int
            :return: A string of n meows, one per line
            :rtype: str
            """
            **return** "meow**\n**" * n
        
        number = int(input("Number: "))
        meows = meow(number)
        print(meows, end="")
        ```
        
    
    Notice how multiple docstring arguments are included. For example, it describes the parameters taken by the function and what is returned by the function.
    
- Established tools, such as [Sphinx](https://www.sphinx-doc.org/en/master/index.html), can be used to parse docstrings and automatically create documentation for us in the form of web pages and PDF files such that you can publish and share with others.
- You can learn more in Python’s documentation of [docstrings](https://peps.python.org/pep-0257/).

## **`[argparse](https://cs50.harvard.edu/python/2022/notes/9/#argparse)`**

Suppose we want to use command-line arguments in our program. In the text editor window, code as follows:

- Code Example
    
    ```python
    **import** sys
    
    **if** len(sys.argv) == 1:
        print("meow")
    **elif** len(sys.argv) == 3 **and** sys.argv[1] == "-n":
        n = int(sys.argv[2])
        **for** _ **in** range(n):
            print("meow")
    **else**:
        print("usage: meows.py [-n NUMBER]")
    ```
    

Notice how `sys` is imported, from which we get access to `sys.argv`—an array of command-line arguments given to our program when run. We can use several `if` statements to check whether the use has run our program properly.

- Let’s assume that this program will be getting much more complicated. How could we check all the arguments that could be inserted by the user? We might give up if we have more than a few command-line arguments!

Luckily, `argparse` is a library that handles all the parsing of complicated strings of command-line arguments. In the text editor window, code as follows:

- Code Example
    
    ```python
    **import** argparse
    
    parser = argparse.**ArgumentParser**()
    parser.add_argument("-n")
    args = parser.parse_args()
    
    **for** _ **in** range(int(args.n)):
        print("meow")
    ```
    

Notice how `argparse` is imported instead of `sys`. An object called `parser` is created from an `ArgumentParser` class. That class’s `add_argument` method is used to tell `argparse` what arguments we should expect from the user when they run our program. Finally, running the parser’s `parse_args` method ensures that all of the arguments have been included properly by the user.

We can further improve this program. In the text editor window, code as follows:

- Code Example
    
    ```python
    **import** argparse
    
    parser = argparse.**ArgumentParser**(description="Meow like a cat")
    parser.add_argument("-n", default=1, help="number of times to meow", type=int)
    args = parser.parse_args()
    
    **for** _ **in** range(args.n):
        print("meow")
    ```
    

Notice how not only is help documentation included, but you can provide a `default` value when no arguments are provided by the user.

- You can learn more in Python’s documentation of `[argparse](https://docs.python.org/3/library/argparse.html)`.
