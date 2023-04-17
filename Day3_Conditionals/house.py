name = input("Whats your name? : ")

# Redundancy is been removed by the keyword MATCH
# if name=="Harry":
#     print("GriffinDor")
# elif name=="Hermione":
#     print("GriffinDor")
# elif name=="Ron":
#     print("GriffinDor")
# elif name=="Draco":
#     print("Slytherin")
# else:
#     print("Who")
match name:
    case "Harry" | "Hermione" | "Ron":    #Read is clear and Program is precise 
        print("GriffinDor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")