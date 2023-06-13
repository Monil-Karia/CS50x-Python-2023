# Unit Tests
We make test cases for the program's to check for the possible bugs and error in the program.

- calculator.py
    
    ```python
    def main():
        x = int(input("Whats x? "))
        print("x squared is" , square(x))
    
    def square(n):
        return n * n
    
    if __name__ == '__main__':
        main()
    ```
    

```python
##test_calculator.py #fortesting the calculator program 
from calculator import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("2 square was not 4")
    if square(3) != 9:
        print("3 square was not 9")

if __name__ == "__main__":
    main()
```

### assert - Python’s `assert` command allows us to tell the compiler that something, some assertion, is true.

- Code Example :
    
    ```python
    from calculator import square
    
    def main():
        test_square()
    
    #It gives the AssertionError for not following the assertion keyword
    
    def test_square():
        try:
            assert square(2) == 4
        except AssertionError:
            print("2 Squared was not 4")
        try: 
            assert square(3) == 9
        except AssertionError:
            print("3 Squared was not 9")
        try: 
            assert square(0) == 0
        except AssertionError:
            print("0 Squared was not 0")
        try: 
            assert square(-2) == 4
        except AssertionError:
            print("-2 Squared was not 4")
        try: 
            assert square(-3) == 9
        except AssertionError:
            print("-3 Squared was not 9")
    
    if __name__ == "__main__":
        main()
    ```
    

AssertionError → It is the error when an assertion statement got failed .

But writing this much lines of code is not feasible and also not very readable for the user , we writing a 10 lines of code in our main and for testing the code we have written a 31 lines of code which is not explanatory for the user to test the code .  

For this kind of work we have some automation tools which does our testing based upon our inputs

### **pytest →**

It is the library which is used for testing purpose of our code , it is different from other’s because of the  predefined modules or the code for testing our code we have to just specify what we want and some things are done by pytest 

- test_cal_pytest.py
    
    ```python
    
    from calculator import square
    
    def test_square():
        assert square(2) == 4
        assert square(3) == 9
        assert square(-2) == 4
        assert square(-3) == 9
        assert square(0) == 0
    
    # No main function
    # No Try and expect 
    # No printing the message
    
    #Output for the running pytest on the file 
    python -m pytest .\test_cal_pytest.py
    ========================================================== test session starts ===========================================================
    platform win32 -- Python 3.11.0, pytest-7.2.0, pluggy-1.0.0
    rootdir: C:\Users\Monil Karia\OneDrive\Desktop\Pyhton Hustle\CS50's Python\Day9_UnitTests
    plugins: anyio-3.6.2
    collected 1 item                                                                                                                          
    
    test_cal_pytest.py F                                                                                                                [100%]
    
    ================================================================ FAILURES ================================================================
    ______________________________________________________________ test_square _______________________________________________________________
    
        def test_square():
            assert square(2) == 4
    >       assert square(3) == 9
    E       assert 6 == 9
    E        +  where 6 = square(3)
    
    test_cal_pytest.py:5: AssertionError
    ======================================================== short test summary info =========================================================
    FAILED test_cal_pytest.py::test_square - assert 6 == 9
    =========================================================== 1 failed in 0.16s ============================================================
    ```
    
    1. Here we can understand that **test_squares** is the failure where our program got wrong 
    2. Now we can see that the assert of square(3) is showing the error and it is giving the output as 6
    3. +   where == 9 shows that instead of giving 9 as an output for the program it is giving 6 
    4. short test summary info → we have that assertion of 9 should be 6 for the program 
    
    <aside>
    💡 Good Logic →
    we imported pytest and then used the keyword raises to raise an error of TypeError if a string is passed in the square function
    
    ```python
    import pytest
    from calculator import square
    
    def test_positive():
        assert square(2) == 4
        assert square(3) == 9
    def test_zero():
        assert square(0) == 0
    def test_negetive():
        assert square(-3) == 9
        assert square(-2) == 4
    def test_str():
        with pytest.raises(TypeError):
            square("cat")
    ```
    
    </aside>
    

### pytest in folders -

- Unit testing code using multiple tests is so common that you have the ability to run a whole folder of tests with a single command.
- First, in the terminal window, execute `mkdir test` to create a folder called `test`.
- Then, to create a test within that folder, type in the terminal window `code test/hello.py`. Notice that `test/` instructs the terminal to create `hello.py` in the folder called `test`.
- In the text editor window, modify the file to include the following code:

```python
**from** hello **import** hello
  
  
**def** test_default():
    **assert** hello() == "hello, world"
  
  
**def** test_argument():
    **assert** hello("David") == "hello, David"
```

Notice that we are creating a test just as we did before.

- `pytest` will not allow us to run tests as a folder simply with this file (or a whole set of files) alone without a special `__init__` file. In your terminal window, create this file by typing `code test/__init__.py`. Note the `test/` as before, as well as the double underscores on either side of `init`. Even leaving this `__init__.py` file empty, `pytest` is informed that the whole folder containing `__init__.py` has tests that can be run.
- Now, typing `pytest test` in the terminal, you can run the entire `test` folder of code.
