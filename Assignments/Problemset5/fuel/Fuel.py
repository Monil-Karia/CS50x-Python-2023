def main():
    input_text = input("Fraction: ")
    print(convert(input_text))


def convert(fraction):
        while True:
            try:
                num1 ,num2 = map(int,fraction.split("/"))
                fraction = (num1/num2) * 100
                return gauge(fraction)
            except(ValueError,ZeroDivisionError):
                fraction = input("Fraction: ")
                continue


def gauge(percentage):
    if(percentage < 1):
        return("E")
    elif(percentage > 99):
        return("F")
    else:
        return(f"{percentage:.2f}%")
    


if __name__ == "__main__":
    main()
