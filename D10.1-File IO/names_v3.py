with open("names.txt" , "r") as file:
    #Beware that readline() is also a function which just reads the lines of the code 
    lines = file.readlines()

for line in lines:
    print("Hello," , line.rstrip())