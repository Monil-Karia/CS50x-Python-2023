class Wizard:
    def __init__(self , name):
        if not name:
            raise ValueError("Missing Name: ")
        self.name = name

class Student(Wizard):  #here wizard acts as a super class for the class Student
    def __init__(self , name , house):
        super().__init__(name) #calling the Wizard class __init__ where it has been wizard called
        # self.name = name # we care calling the wizard calss and using the inheritance of the OOPs
        self.house = house
    
    ...


class Professor(Wizard): #here wizard acts as a super class for the class professor
    def __init__(self,name ,subject):
        super().__init__(name)
        # self.name = name # we care calling the wizard calss and using the inheritance of the OOPs
        self.subject = subject
    
    ...


wizard = Wizard("Albus")
student = Student("harry","Gryffindor")
professor = Professor("Serverus","Defense against Dark Arts")
