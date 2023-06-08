# OOPs concepts in Python

Functional Programming - Uses of Functions in the program 

- tuple → its a collection of  values and its a immutable (we cant change the values) .
    
    ```python
    def main():
        student = get_student()
        if student[0] == "Padma":
            student[1] = "RavenClaw"
            
        print(f"{student[0]} from {student[1]}")
    
    def get_student():
        name = input("Name: ")
        house = input("House: ")
        return name, house #here we are using tuples not the  
    # using tuple we can increase the correctness of the variables we use in the program 
    
    if __name__ == "__main__":
        main()
    ```
    
    - Here in this program we get an TypeError:’tuple’ object does not support item assigment - here it means that  that tuple is immutable and it can’t change in the program .

### Classes → It allows us to give a name to our own data type

```python
class Student:
    ...
def main():
    student = get_student()
    if student["name"] =="Padma":
        student["house"] = "RavenClaw"
    
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()
```

### Object → An **Object** is an instance of a Class.

for example you can say that the class is the mold of an house and by object we can use the mold to create house from it .

```python
class Student:
    ...  #Here we have used 3 dots to show that we can come to this function later 
def main():
    student = get_student()
    if student["name"] =="Padma":
        student["house"] = "RavenClaw"
    
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()
```

### method → this are the function in classes to define a behaviors’ of that particular function

```python
class Student:
    def __init__(self , name , house): #instance variable to objects
        self.name = name
        self.house =house
def main():
    student = get_student()
    
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name,house)   #Constructor Call for the Student object 
    return student

if __name__ == "__main__":
    main()
```

Here we can that init is used and that kind of cryptic but the logic here is init is for initializing and its  making an constructor here of the same class we made and its initiazing the value of name and house to its self so that when we call it it just initializes the name and hous

- Some More of the Code for advance learning in Classes
    
    ```python
    import emoji
    
    class Student:
        def __init__(self , name , house , patronus): #instance variable to objects
            if not name:
                raise ValueError("Missing Name") #We have raised a ValueError 
            if house not in ["Gryffindor", "HufflePuff" , "RavgenClaww" , "Slytherin"]:
                raise ValueError("Invlaid house")
            
            self.name = name
            self.house =house
            self.patronus = patronus
        
        def __str__(self): # it is to return the string value for the function and called by default
            return f"{self.name} from {self.house}"
        
        def charm(self):
            match self.patronus:
                case "Stag":
                    return ""
                case "Otter":
                    return ""
                case "Jack rusell terrier":
                    return emoji.emojize(':dog:' ,language = 'alias')
                case _:
                    return "/"
    
            
    
    def main():
        student = get_student()    
        print(student)
        print(student.charm())
    
    def get_student():
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ")
        return  Student(name,house,patronus)   #Constructor Call for the Student object 
    
    if __name__ == "__main__":
        main()
    ```
