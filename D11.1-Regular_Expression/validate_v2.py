import re

email = input("What your Emaill? ")
#.+ @ .+ means we assigned that after and before the @ we have strings that 
if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|gov|net|org)$",email , re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")