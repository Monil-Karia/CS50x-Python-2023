#code with except and try 
while True:
    try:
        x = int(input("What is x? "))
    except ValueError:
        print("x is not an Integer")
    else:
        break

print(f"x is {x}")

# WE CAN WRITE THE CODE IN THIS OTHER WAY AS LOGICALLLY IT IS SAME 
'''
while True:
    try:
        x = int(input("What is x? "))
        break
    except ValueError:
        print("x is not an Integer")

print(f"x is {x}")
'''