x = int(input("Write ur x? "))  
y = int(input("Write ur y? "))

#Do we really need z variable ? No
# z = int(x) + int(y)

print(x + y) 

## Float and round

x = float(input("Write ur x? "))  
y = float(input("Write ur y? "))

z = round(x + y)

print(f"{z:,}")

z1 = x / y 

print(f"{z:.2f}")