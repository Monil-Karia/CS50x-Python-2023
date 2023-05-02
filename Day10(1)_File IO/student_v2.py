students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        # one liner code
        student = {"name": name, "house": house}
        # same as above code but mor lines
        # student["name"] = name
        # student["house"] = house
        students.append(student)


def get_name(student):
    return student["name"]


# not passing parenthesis beacuse sorted will call it by itself and also
for student in sorted(students, key=lambda student: student["name"]):
    # Why Single Quote?
    # In dict when we use to index in it then we use the single quote instead of double
    #
    print(f"{student['name']} is in {student['house']}")
