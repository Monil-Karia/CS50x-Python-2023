## Day 1 → Functions & Variables

1. Problem statement : In a file called `indoor.py`, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a `str` of your own as an argument to `input`.
2. Problem statement : In a file called `playback.py`, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with `...` (i.e., three periods).
3. Problem statement : In a file called faces.py , implement a function called convert that accepts a str as input and returns that same input with any :) converted to 😊 and any :( converted to 😟
    
    All other text should be returned unchanged.
    
    Then, in that same file, implement a function called `main` that prompts the user for input, calls `convert` on that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a `str` of your own as an argument to `input`. Be sure to call `main` at the bottom of your file.
    
4. Problem statement : In a file called `einstein.py` , implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer. 
Hint: E =mc^2
5.  In the United States, it’s customary to leave a tip for your server after dining in a restaurant, typically an amount equal to 15% or more of your meal’s cost. Not to worry, though, we’ve written a tip calculator for you, below!
    
    ```python
    **def** main():
        dollars = dollars_to_float(input("How much was the meal? "))
        percent = percent_to_float(input("What percentage would you like to tip? "))
        tip = dollars * percent
        print(f"Leave $**{**tip**:**.2f**}**")
    
    **def** dollars_to_float(d):
        *# TODO*
    **def** percent_to_float(p):
        *# TODO*
    main()
    ```
    
    Well, we’ve written *most* of a tip calculator for you. Unfortunately, we didn’t have time to implement two functions:
    
    - `dollars_to_float`, which should accept a `str` as input (formatted as `$##.##`, wherein each `#` is a decimal digit), remove the leading `$`, and return the amount as a `float`. For instance, given `$50.00` as input, it should return `50.0`.
    - `percent_to_float`, which should accept a `str` as input (formatted as `##%`, wherein each `#` is a decimal digit), remove the trailing `%`, and return the percentage as a `float`. For instance, given `15%` as input, it should return `0.15`.
    
    Assume that the user will input values in the expected formats.
