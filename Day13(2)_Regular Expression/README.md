# REGEX DAY 2
- re.**match**(*pattern*, *string*, *flags=0*)
    
    If zero or more characters at the beginning of *string* match the regular expression *pattern*, return a corresponding [match object](https://docs.python.org/3/library/re.html?highlight=re%20match#match-objects). Return `None` if the string does not match the pattern; note that this is different from a zero-length match.
    
- re.**fullmatch**(*pattern*, *string*, *flags=0*)
    
    If the whole *string* matches the regular expression *pattern*, return a corresponding [match object](https://docs.python.org/3/library/re.html?highlight=re%20match#match-objects). Return `None` if the string does not match the pattern; note that this is different from a zero-length match.
    

```python
import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$" , name)
if matches:
    last , first = matches.groups()
    name = f"{first} {last}"
print(f"hello,{name}")
```

- Working of the code →
    
    This is a Python code that prompts the user to enter their name, then uses the regular expression module **`re`** to extract and rearrange the name into a standard format.
    
    The first line of the code imports the **`re`** module, which provides support for regular expressions in Python.
    
    The second line uses the **`input`** function to prompt the user to enter their name. The **`strip`** method is called on the input to remove any leading or trailing whitespace characters.
    
    The third line uses the **`re.search`** method to search for a pattern in the user's input. The pattern is defined as **`^(.+), (.+)$`**, which matches a string that starts with one or more characters, followed by a comma and a space, and then ends with one or more characters. The parentheses in the pattern define two groups that match the last and first names, respectively.
    
    If the **`re.search`** method finds a match, the fourth line uses tuple unpacking to assign the matched groups to the **`last`** and **`first`** variables. The fifth line then reassigns the **`name`** variable with the rearranged name using an f-string, which interpolates the values of the **`first`** and **`last`** variables into a new string with the format **`"{first} {last}"`**.
    
    Finally, the last line prints a personalized greeting message that includes the rearranged name using an f-string with the **`print`** function. If the regular expression doesn't match the input, the name entered by the user is printed as is without any changes.
    

: = → Walrus Operator → The walrus operator is useful when you want to evaluate an expression and assign the result to a variable at the same time

- re.**search**(*pattern*, *string*, *flags=0*)
    
    Scan through *string* looking for the first location where the regular expression *pattern* produces a match, and return a corresponding [match object](https://docs.python.org/3/library/re.html?highlight=re%20search#match-objects). Return `None` if no position in the string matches the pattern; note that this is different from finding a zero-length match at some point in the string.
