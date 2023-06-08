import emoji

class Student:
    def __init__(self , name , house): #instance variable to objects    
        self.name = name
        self.house =house  #Calling the Setter method 
    
    def __str__(self): # it is to return the string value for the function and called by default
        return f"{self.name} from {self.house}"
    
    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name
    
    #Getter -> function for class where it 'gets' some value
    @property 
    def house(self):  #getter always has the one argument in the function
        return self._house
    
    #Setter ->  function for class where it 'sets' some value
    @house.setter   #setter has one argument + another argument for the setting
    def house(self,house):
        if house not in ["Gryffindor", "HufflePuff" , "RavgenClaww" , "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house
    #self.house is instance variable of the function 

    @classmethod
    def get(cls): 
        name = input("Name: ")
        house = input("House: ")
        return  Student(name,house)
        

def main():
    student = Student.get()
    # student.house = "Number Four, Privet Drive" # We can explicitly call the house and it changes the value of the house 
    print(student)

if __name__ == "__main__":
    main()
 
