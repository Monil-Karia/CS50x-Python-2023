students = ["Hermoine" , "Harry" , "Ron"]

print(students)     #Output -> ['Hermoine', 'Harry', 'Ron']

for i in range(len(students)):   #we used Student as we r gonna used in print statment
    print(i+ 1, students[i])

print("\n")

#How we define the lists in the python 
students_new=["Hermoine" , "Harry" , "Ron" , "Draco"]
houses = ["GriffinDor" , "GriffinDor" , "Griffindor" , "Slytherin" ]

#Now we are using dict as per our use name= {key : value}
students = {
    "Hermoine": "Gryffindor",
    "Harry" : "Gryffindor" , 
    "Ron" : "Gryffindor" , 
    "Draco" : "Slytherin"
}

for student in students:
    print(student , students[student] ,  sep =" , ")

print("\n")

#What if we have more than 2 value we have more values
#name , house , patronas

students_adv=[   #as it have square brackets so it is a list , {} is dictonary
    { "name":"Hermione" , "house":"Gryffindor" , "patronus":"Otter"} , 
    { "name":"Harry" , "house":"Gryffindor" , "patronus":"Stag"} , 
    { "name":"Ron" , "house":"Gryffindor" , "patronus":"jack Rusell terrier"} , 
    { "name":"Draco" , "house":"Slytherin" , "patronus": None}
]

for student in students_adv:
    print(student["name"] ,student["house"] , student["patronus"] , sep = " , ")   #value of the name key