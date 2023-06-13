
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

price = 0

while True:
    try:
        input_text = input("Item: ").title()
        for k in menu:
            if(k == input_text):
                price += menu[k] 
                print(f"Total: {price}")
    except(KeyError):
        print("key not found")
    except(EOFError):
        break
    