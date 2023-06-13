students = [
    {"name" : "Hermoine" , "house": "Gryffindor"},
    {"name" : "Harry" , "house": "Gryffindor"},
    {"name" : "Ron" , "house": "Gryffindor"},
    {"name" : "Draco" , "house": "Slytherin"},
    {"name" : "Padma" , "house": "RavenClaw"},
]

houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house) 