import csv

students = []

with open("students.csv") as file:
    # it will figure out that where are the commas and what is the format of the file
    #reader function of csv returns list 
    #dict reader returns DICTionary
    reader = csv.DictReader(file) 
    for row in reader:
        students.append({"name" : row["name"], "home": row["home"]})

for student in sorted(students, key = lambda students:students["name"]):
        print(f"{student['name']} is from {student['home']}")