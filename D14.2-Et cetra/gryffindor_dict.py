students = ["Hermoine" , "Harry" , "Ron"]

gryffindors = [{"name":student , "house": "Gryffindor"} for student in students] #Dict Comprehensions
gryffindors_v2 = {student:"Gryffindor" for student in students} 

print(gryffindors)
print(gryffindors_v2)