names = []

for _ in range(3):
    name = input("What's your name? ")
    names.append(name)         #We can tight it further names.append(input("What's Your name? "))


#Sorted is the keyword to use to sort the list of names
for name in sorted(names):
    print(f"Hello, {name}")
