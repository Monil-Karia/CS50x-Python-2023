# Et-cetra Day2 
## **[Unpacking](https://cs50.harvard.edu/python/2022/notes/9/#unpacking)**

Notice how this program tries to get a user’s first name by naively splitting on a single space.

- This is getting quite verbose. Wouldn’t it be nice if we could simply pass the list of coins to our function?

To enable the possibility of passing the entire list, we can use unpacking. In the text editor window, code as follows:

- Code Example
    
    ```python
    **def** total(galleons, sickles, knuts):
        return (galleons * 17 + sickles) * 29 + knuts
    
    coins = [100, 50, 25]
    
    print(total(*coins), "Knuts")
    ```
    

Notice how a `*` unpacks the sequence of the list of coins and passes in each of its individual elements to `total`.

When you start talking about “names” and “values,” dictionaries might start coming to mind! You can implement this as a dictionary. In the text editor window, code as follows:

- Code Example
    
    ```python
    **def** total(galleons, sickles, knuts):
        return (galleons * 17 + sickles) * 29 + knuts
    
    coins = {"galleons": 100, "sickles": 50, "knuts": 25}
    
    print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")
    ```
    

Notice how a dictionary called `coins` is provided. We can index into it using keys, such as “galleons” or “sickles”.

Since the `total` function expects three arguments, we cannot pass in a dictionary. We can use unpacking to help with this. In the text editor window, code as follows:

- Code Example
    
    ```python
    **def** total(galleons, sickles, knuts):
        return (galleons * 17 + sickles) * 29 + knuts
    
    coins = {"galleons": 100, "sickles": 50, "knuts": 25}
    
    print(total(**coins), "Knuts")
    ```
    

Notice how `**` allows you to unpack a dictionary. When unpacking a dictionary, it provides both the keys and values.

## **`[args` and `kwargs`](https://cs50.harvard.edu/python/2022/notes/9/#args-and-kwargs)**

Recall the `print` documentation we looked at earlier in this course:

`print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`

- `args` are positional arguments, such as those we provide to print like `print("Hello", "World")`.
- `kwargs` are named arguments, or “keyword arguments”, such as those we provide to print like `print(end="")`.

As we see in the prototype for the `print` function above, we can tell our function to expect a presently unknown number positional arguments. We can also tell it to expect a presently unknown number of keyword arguments. In the text editor window, code as follows:

- Code Example
    
    ```python
    **def** f(*args, **kwargs):
        print("Positional:", args)
    
    f(100, 50, 25)
    ```
    

Notice how executing this code will be printed as positional arguments.

Notice how the named values are provided in the form of a dictionary.

- Thinking about the `print` function above, you can see how `objects` takes any number of positional arguments.
- You can learn more in Python’s documentation of `[print](https://docs.python.org/3/library/functions.html#print)`.

## **`[map](https://cs50.harvard.edu/python/2022/notes/9/#map)`**

Wouldn’t it be nice to yell a list of unlimited words? Modify your code as follows:

- Code Example
    
    ```python
    **def** main():
        yell(["This", "is", "CS50"])
    
    **def** yell(words):
        uppercased = []
        **for** word **in** words:
            uppercased.append(word.upper())
        print(*uppercased)
    
    **if** __name__ == "__main__":
        main()
    ```
    

Notice we accumulate the uppercase words, iterating over each of the words and uppercasing them. The uppercase list is printed utilizing the `*` to unpack it.

Removing the brackets, we can pass the words in as arguments. In the text editor window, code as follows:

- Code Example
    
    ```python
    **def** main():
        yell("This", "is", "CS50")
    
    **def** yell(*words):
        uppercased = []
        **for** word **in** words:
            uppercased.append(word.upper())
        print(*uppercased)
    
    **if** __name__ == "__main__":
        main()
    ```
    

Notice how `*words` allows for many arguments to be taken by the function.

- You can learn more in Python’s documentation of `[map](https://docs.python.org/3/library/functions.html#map)`.

## **[List Comprehensions](https://cs50.harvard.edu/python/2022/notes/9/#list-comprehensions)**

- List comprehensions allow you to create a list on the fly in one elegant one-liner.

We can implement this in our code as follows:

- Code Example
    
    ```python
    **def** main():
        yell("This", "is", "CS50")
    
    **def** yell(*words):
        uppercased = [arg.upper() **for** arg **in** words]
        print(*uppercased)
    
    **if** __name__ == "__main__":
        main()
    ```
    

Notice how instead of using `map`, we write a Python expression within square brackets. For each argument, `.upper` is applied to it.

- Taking this concept further, let’s pivot toward another program.

More elegantly, we can simplify this code with a list comprehension as follows:

- Code Example
    
    ```python
    students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"},
    ]
    
    gryffindors = [
        student["name"] **for** student **in** students **if** student["house"] == "Gryffindor"
    ]
    
    **for** gryffindor **in** sorted(gryffindors):
        print(gryffindor)
    ```
    

Notice how the list comprehension is on a single line!

## **`[filter](https://cs50.harvard.edu/python/2022/notes/9/#filter)`**

- Using Python’s `filter` function allows us to return a subset of a sequence for which a certain condition is true.

Notice how a function called `is_gryffindor` is created. This is our filtering function that will take a student `s`, and return `True` or `False` depending on whether the student’s house is Gryffindor. You can see the new `filter` function takes two arguments. First, it takes the function that will be applied to each element in a sequence—in this case, `is_gryffindor`. Second, it takes the sequence to which it will apply the filtering function—in this case, `students`. In `gryffindors`, we should see only those students who are in Gryffindor.

- Code Example
    
    ```python
    # `filter` can also use lambda functions as follows:
    
    `students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"},
    ]
    
    gryffindors = filter(**lambda** s: s["house"] == "Gryffindor", students)
    
    **for** gryffindor **in** sorted(gryffindors, key=**lambda** s: s["name"]):
        print(gryffindor["name"])`
    ```
    

Notice how the same list of students is provided.

- You can learn more in Python’s documentation of `[filter](https://docs.python.org/3/library/functions.html#filter)`.

## **[Dictionary Comprehensions](https://cs50.harvard.edu/python/2022/notes/9/#dictionary-comprehensions)**

Notice how this code doesn’t (yet!) use any comprehensions. Instead, it follows the same paradigms we have seen before.

We can now apply dictionary comprehensions by modifying our code as follows:

- Code Example
    
    ```python
    students = ["Hermione", "Harry", "Ron"]
    
    gryffindors = [{"name": student, "house": "Gryffindor"} **for** student **in** students]
    
    print(gryffindors)
    ```
    

Notice how all the prior code is simplified into a single line where the structure of the dictionary is provided for each `student` in `students`.

We can even simplify further as follows:

- Code Example
    
    ```python
    students = ["Hermione", "Harry", "Ron"]
    
    gryffindors = {student: "Gryffindor" **for** student **in** students}
    
    print(gryffindors)
    ```
    

Notice how the dictionary will be constructed with key-value pairs.

## **`[enumerate](https://cs50.harvard.edu/python/2022/notes/9/#enumerate)`**

Notice how each student is enumerated when running this code.

Utilizing enumeration, we can do the same:

- Code Example
    
    ```python
    students = ["Hermione", "Harry", "Ron"]
    
    **for** i, student **in** enumerate(students):
        print(i + 1, student)
    ```
    

Notice how enumerate presents the index and the value of each `student`.

You can learn more in Python’s documentation of `[enumerate](https://docs.python.org/3/library/functions.html#enumerate)`.

## **[Generators and Iterators](https://cs50.harvard.edu/python/2022/notes/9/#generators-and-iterators)**

- In Python, there is a way to protect against your system running out of resources the problems they are addressing become too large.

We can call a sheep function by modifying our code as follows:

- Code Example
    
    ```python
    **def** main():
        n = int(input("What's n? "))
        **for** i **in** range(n):
            print(sheep(i))
    
    **def** sheep(n):
        **return** "" * n
    
    **if** __name__ == "__main__":
        main()
    ```
    

Notice how the `main` function does the iteration.

We can provide the `sheep` function more abilities. In the text editor window, code as follows:

- Code Example
    
    ```python
    **def** main():
        n = int(input("What's n? "))
        **for** s **in** sheep(n):
            print(s)
    
    **def** sheep(n):
        flock = []
        **for** i **in** range(n):
            flock.append("" * i)
        **return** flock
    
    **if** __name__ == "__main__":
        main()
    ```
    

Notice how we create a flock of sheep and return the `flock`.

- Executing our code, you might try different numbers of sheep such as `10`, `1000`, and `10000`. What if you asked for `1000000` sheep, your program might completely hang or crash. Because you have attempted to generate a massive list of sheep, your computer may be struggling to complete the computation.

The `yield` generator can solve this problem by returning a small bit of the results at a time. In the text editor window, code as follows:

- Code Example
    
    ```python
    **def** main():
        n = int(input("What's n? "))
        **for** s **in** sheep(n):
            print(s)
    
    **def** sheep(n):
        **for** i **in** range(n):
            **yield** "" * i
    
    **if** __name__ == "__main__":
        main()
    ```
    

Notice how `yield` provides only one value at a time while the `for` loop keeps working.

- You can learn more in Python’s documentation of [generators](https://docs.python.org/3/howto/functional.html#generators).
- You can learn more in Python’s documentation of [iterators](https://docs.python.org/3/howto/functional.html#iterators).

## **[Congratulations!](https://cs50.harvard.edu/python/2022/notes/9/#congratulations)**

- As you exit from this course, you have more of a mental model and toolbox to address programming-related problems.
- First, you learned about functions and variables.
- Second, you learned about conditionals.
- Third, you learned about loops.
- Fourth, you learned about exceptions.
- Fifth, you learned about libraries.
- Sixth, you learned about unit tests.
- Seventh, you learned about file I/O.
- Eighth, you learned about regular expressions.
- Most recently, you learned about object-oriented programming.
- Today, you learned about many other tools you can use.
