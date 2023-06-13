input_text = input("Item: ")

fruits = {
    "Apple" : "130" , 
    "Banana" : "110" , 
    "Avocado" : "50" , 
    "Grapefruit" : "90" , 
    "Honeydew" : "50" , 
    "Kiwifruit" : "90" , 
    "Lemon" : "20" , 
    "Pineapple" : "50"
}

for k in fruits:
    if k == input_text:
        print(f"Calories : {fruits[k]}")