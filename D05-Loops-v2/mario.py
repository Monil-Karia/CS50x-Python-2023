def main():
    print_column(3)
    print_row(5)
    print_square(3)
    square_newlogic(5)

def print_column(height):
    for _ in range(height):
        print("#")
## we can write print("#\n * height , end="")

def print_row(length):
    for _ in range(length):
        print("#" , end ="")
    print()


#FOr each row in square 
def print_square(size):
    print(f"Printing the Square of {size}")
    for row in range(size):

        #for each row in the square
        for column in range(size):

            #printing the brick of mario
            print("#", end="")

        #printing the next line for the column
        print()

def square_newlogic(size):
    for row in range(size):
        print_row(size)

main()