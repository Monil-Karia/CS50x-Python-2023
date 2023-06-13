#To make a more usable code we pass the parameter of the function in the main 
# and use the argument in the get int
def main():
    x = get_int("Whats the x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            #Optimising to the max in the same line 
            # We are gettiing more dynamic and using the whats the user want and not the function 
            return int(input(prompt))
        except ValueError:
            print("x is not an Integer")



main()