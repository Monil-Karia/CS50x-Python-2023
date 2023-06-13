import csv

name  = input("Whats Your name? ")
home  = input("Where's your home? ")

with open("student_v2.csv" , "a") as file:
    writer = csv.DictWriter(file , fieldnames=["name", "home"])
    writer.writerow({"name" : name , "home": home})