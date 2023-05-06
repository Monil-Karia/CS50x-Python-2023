# Regular Expression (REGEX)
regexes → Capability to define patterns in the code to match on some kind of data. It may to validate it or just to clean up . 

### re → Library for Regular Expression

- Docs → [https://docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html)
- We will use main function search → re.**search**(*pattern*, *string*, *flags=0*)
    - Scan through *string* looking for the first location where the regular expression *pattern* produces a match, and return a corresponding [match object](https://docs.python.org/3/library/re.html#match-objects). Return `None` if no position in the string matches the pattern; note that this is different from finding a zero-length match at some point in the string.
- Code Example →
    
    ```python
    import re
    
    email = input("What your Emaill? ")
    #.+ @ .+ means we assigned that after and before the @ we have strings that 
    if re.search(".+@.+",email):
        print("Valid")
    else:
        print("Invalid")
    ```
    

Here in the program we can see that + is used as well as . is used to check that there are strings before and after the @ to validate the Email address.    

- In the search function we have some special functions we have:
    - . → any character except newline
    - '*' → 0 or more reptations
    - '+' →1 or more reptations
    - ? → 0 or 1 reptations
    - {m} → m for reptations
    - {m,n} → m - n reptations
        - Code Example
            
            ```python
            if re.search(r".+@.+\.edu",email):
                print("Valid")
            # Here r indicates is raw string means we are passing the string as raw string 
            ```
            
    - ^ → matches starts of the string
    - $ → matches the end of the string or just before the newline at the end of the string
        - Code example :
            
            ```python
            if re.search(r"^.+@.+\.edu$",email):
                print("Valid")
            ```
            
    - '[ ]' → Set of characters
    - [ ^ ] → complementing the set  (except)
        - Code Example →
            
            ```python
            
            import re
            
            email = input("What your Emaill? ")
            
            # here we are [ ] using this to accept certain characters which are a-z 
            # and A-Z and 0-9 and _ these are used without the space and program understands
            if re.search(r"^[a-zA-Z0-9_]+@[^@]+\.edu$",email):
                print("Valid")
            else:
                print("Invalid")
            ```
            
    - \w → Used for the Alphanumeric character and the _ included in it so here we can replace [a-zA-Z0-9_] with \w
    - \d → for decimal digit (0-9)
    - \D → anything not a decimal digit
    - \s → white space character (tab on keyboard)
    - \S → not a Whitespace character
    - \w → word character …as well as numbers and the underscore
    - \W → not a word characters
    - A | B → either A or B
    - ( . . . ) → a group
    - (?: . . . ) non -capturing versions

### We are using the by-default flags in re library

- re.IGNORECASE → Perform case-insensitive matching; expressions like `[A-Z]` will also match lowercase letters
- re.MULTILINE → When specified, the pattern character `'^'` matches at the beginning of the string and at the beginning of each line (immediately following each newline); and the pattern character `'$'` matches at the end of the string and at the end of each line (immediately preceding each newline). By default, `'^'` matches only at the beginning of the string, and `'$'` only at the end of the string and immediately before the newline (if any) at the end of the string. Corresponds to the inline flag `(?m)`.
- re.DOTALL → Make the `'.'` special character match any character at all, including a newline; without this flag, `'.'` will match anything *except* a newline. Corresponds to the inline flag `(?s)`.
    - Code Example →
        
        ```python
        **import** re
        
        email = input("What's your email? ").strip()
        
        **if** re.search(r"^\w+@\w.+\.edu$", email, re.IGNORECASE):
            print("Valid")
        **else**:
            print("Invalid")
        ```
        
        Notice how we added a third parameter `re.IGNORECASE`. Running this program with `MALAN@HARVARD.EDU`, the input is now considered valid.
        

```python

#Whole thing in paranthesis can be there or cant be there as per the ? 
#Still very cryptic in nature but good to go 
if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|gov|net|org)$",email , re.IGNORECASE):
    print("Valid")
```

- There are other functions within the `re` library you might find useful. `re.match` and `re.fullmatch` are ones you might find exceedingly useful.
- You can learn more in Python’s documentation of [re](https://docs.python.org/3/library/re.html).

```html
#Original regex will look like a for validating the email address will be -> 
^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$
```
