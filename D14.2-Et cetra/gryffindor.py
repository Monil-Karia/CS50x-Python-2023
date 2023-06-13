students = [
    {"Name":"Hermoine" , "House":"Gryffindor"},
    {"Name":"Harry" , "House":"Gryffindor"},
    {"Name":"Ron" , "House":"Gryffindor"},
    {"Name":"Draco" , "House":"Slytherin"},
]

def is_gryffindor(s):
    return s["House"] == "Gryffindor"

gryffindors = filter(is_gryffindor,students) #Usage of Filter 

for gryffindor in sorted(gryffindors , key=lambda s: s["Name"]):
    print(gryffindor["Name"])

# gryffindors = [
#     student["Name"] for student in students if student["House"] == "Gryffindor"
# ]

# for gryffindor in sorted(gryffindors): 
#     print(gryffindor)