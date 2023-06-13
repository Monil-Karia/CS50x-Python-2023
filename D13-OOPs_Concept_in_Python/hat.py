import random

class Hat:
    # def __init__(self): #selfis related to the object means when the object is called self is called 
    houses = ["Gryffindor", "HufflePuff" , "RavgenClaww" , "Slytherin"]
    
    @classmethod
    def sort(cls,name):
        house = random.choice(cls.houses)
        print(name,"is in",house)



# hat = Hat()     #calling the object
Hat.sort("Harry")