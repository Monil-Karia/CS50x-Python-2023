#use of Arithmetic Symbols use of % (MODULO)

def main():
    numberX = int(input("Input: "))
    is_even(numberX)
    numberY = int(input("Input: "))
    singleline_even(numberY)


def is_even(X):
    if(X % 2 == 0):
        print("Number is Even")
    else:
        print("Number is Odd")

def singleline_even(Y):
    return "Even" if Y % 2 == 0 else "ODD"

# def mindblowing(Z)
#     return (Z % 2 == 0)   # Returns TRUE and FALSE based on condition

main()