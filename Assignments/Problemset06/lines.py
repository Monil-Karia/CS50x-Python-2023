import sys

count = 0

def numof_Lines():
    ...
    

if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
    with open(sys.argv[1],'r') as file:
        Lines = file.readlines()   #It return a list of the lines present in the program
        print(Lines)
        for line in Lines:        #it is iterating the line in the list caled Lines
            print(line.strip())       
            if(line.startswith("#")):
                count += 0
            else:
                count += 1
    print(count)          
elif len(sys.argv) < 2:
    sys.exit("Too few command line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command line arguments")
else:
    sys.exit("Not a python file")

