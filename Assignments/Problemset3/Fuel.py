
while True:
    try:
        input_text = input("Fraction : ")
        num1 ,num2 = input_text.split("/")   #alternative: map(int, input_text.split("/"))
        num1 = int(num1)
        num2 = int(num2)
        fraction = (num1/num2) * 100
        break
    except(ValueError,ZeroDivisionError):
        print("This is a value error or Zero Division error")

print(f"{fraction}%")