import emoji

class Student:
    def __init__(self , name , house): #instance variable to objects
        if not name:
            raise ValueError("Missing Name") #We have raised a ValueError 
        if house not in ["Gryffindor", "HufflePuff" , "RavgenClaww" , "Slytherin"]:
            raise ValueError("Invlaid house")
        
        self.name = name
        self.house =house
    
    def __str__(self): # it is to return the string value for the function and called by default
        return f"{self.name} from {self.house}"


def main():
    student = get_student()   
    student.house = "Number Four, Privet Drive" # We can explicitly call the house and it can 
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return  Student(name,house)   #Constructor Call for the Student object 


if __name__ == "__main__":
    main()
 
