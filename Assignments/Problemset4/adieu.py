import inflect

p = inflect.engine()
name = []

while True:
    try:
        input_text = input("Name: ")
        name.append(input_text)
    except EOFError:
        break

mylist = []
mylist = p.join((name), final_sep="")

print("Adieu, adieu, to " + mylist)
