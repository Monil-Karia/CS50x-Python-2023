amount = 50
while(amount > 0):
    change = int(input("Insert Coin: "))
    amount -= change
    print (f"Amount Due : {amount}")

print("change owned = 0") 