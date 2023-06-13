# OOPs Concept in Python Part-2
## Properties → @property

properties → These are some of the Attributes where we define something to prevent programmers or the users to messing the functions up or program. 

- Code Example
    
    ```python
    import emoji
    
    class Student:
        def __init__(self , name , house): #instance variable to objects
            if not name:
                raise ValueError("Missing Name") #We have raised a ValueError 
            
            self.name = name
            self.house =house  #Calling the Setter method 
        
        def __str__(self): # it is to return the string value for the function and called by default
            return f"{self.name} from {self.house}"
        
        #Getter -> function for class where it 'gets' some value
        @property 
        def house(self):
            return self._house
        
        #Setter ->  function for class where it 'sets' some value
        @house.setter
        def house(self,house):
            if house not in ["Gryffindor", "HufflePuff" , "RavgenClaww" , "Slytherin"]:
                raise ValueError("Invalid House")
            self._house = house
        #self.house is instance variable of the function 
    
    def main():
        student = get_student()   
        # student.house = "Number Four, Privet Drive" # We can explicitly call the house and it changes the value of the house 
        print(student)
    
    def get_student():
        name = input("Name: ")
        house = input("House: ")
        return  Student(name,house)   #Constructor Call for the Student object 
    
    if __name__ == "__main__":
        main()
    ```
    

## decorators

Decorators→ These are the functions which modify the behaviour of other functions . 

<aside>
💡 int is a class → class int(x, base=10)
str is also a class → class str (object=’ ‘)
str.lower() , str.strip() → this are the methods of the class str
list is also a class → class list ([iterable]) 
list.append(x) is a method

</aside>

## class methods → @classmethod

class methods → Here we define that the no matter what the object is calling or the object is passing the arguments the class methods are the mehods which are assoisiated with class no matter what class methods are those whihc dont change with any ohter factors of objects .

- Code Example
    
    ```python
    @classmethod
        def sort(cls,name):  #cls is defined for the class for classmethod
            house = random.choice(cls.houses)
            print(name,"is in",house)
    
    #calling function for the classmethods
    Hat.sort("Harry")
    ```
    

## static methods →

- It turns out that besides `@classmethod`s, which are distinct from instance methods, there are other types of methods as well.
- Using `@staticmethod` may be something you might wish to explore. While not covered explicitly in this course, you are welcome to go and learn more about static methods and their distinction from class methods.

## inheritance

- inheritance → it is the hierarchy that we can incoporate the other classes from the other location
- Inheritance is, perhaps, the most powerful feature of object-oriented programming.
- It just so happens that you can create a class that “inherits” methods, variables, and attributes from another class.

## Exceptions

- While we have just introduced inheritance, we have been using this all along during our use of exceptions.
- It just so happens that exceptions come in a heirarchy, where there are children, parent, and grandparent classes. These are illustrated below:
    
    `BaseException
     +-- KeyboardInterrupt
     +-- Exception
          +-- ArithmeticError
          |    +-- ZeroDivisionError
          +-- AssertionError
          +-- AttributeError
          +-- EOFError
          +-- ImportError
          |    +-- ModuleNotFoundError
          +-- LookupError
          |    +-- KeyError
          +-- NameError
          +-- SyntaxError
          |    +-- IndentationError
          +-- ValueError
     ...`
    
- You can learn more in Python’s documentation of [exceptions](https://docs.python.org/3/library/exceptions.html).

## Operator Overloading

Some operators such as `+` and `-` can be “overloaded” such that they can have more abilities beyond simple arithmetic.

- Code
    
    ```python
    ## Vault.py
    class Vault:
        def __init__(self , galleons = 0, sickles = 0 , knuts = 0):
            self.galleons = galleons
            self.sickles = sickles
            self.knuts = knuts
        def __str__(self):
            return f"{self.galleons} Galleons , {self.knuts} Knuts , {self.sickles} Sickels"
    
        def __add__(self,other): #by default is going to be called we overload the add 
            galleons = self.galleons + other.galleons
            sickles = self.sickles + other.sickles
            knuts = self.knuts + other.knuts
            return Vault(galleons ,sickles , knuts)\
    
    potter = Vault(100,50,25)
    print(potter)
    
    weasly = Vault(25,50,100)
    print(weasly)
    
    #special methods in the Python we use for the object.__add__(self,other)
    
    total = potter + weasly #operator overloading happening here 
    print(total)
    
    # The method we usually go the brute forace method
    # galleons = potter.galleons + weasly.galleons 
    # knuts = potter.knuts + weasly.knuts 
    # sickels = potter.sickles + weasly.sickles
    
    # total = Vault(galleons , sickels , knuts )
    # print(total)
    ```
