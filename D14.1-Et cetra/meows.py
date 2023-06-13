MEOWS = 3   #capitalizing the word it means that the MEOWS is const 
#rather wec can change the value of the MEOWS 


class Cat:
    MEOWS = 3 #It works as the same as const as it is a class variable 

    def meow(self):
        for _ in range(MEOWS):
            print("Meow")


cat = Cat()
cat.meow()