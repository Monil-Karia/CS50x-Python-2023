#Improved version of the names_v3 for each line in a file we are printing it in 
with open("names.txt" , "r") as file:
    for line in file:
        print("Hello, ", line.rstrip())