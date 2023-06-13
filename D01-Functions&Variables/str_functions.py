#ask user for thier name
name = input("Whats your name? ").strip().title()

'''
spliting the name into three parts
passing an argument that computer will recognise that where to split 
'''
first , middle, last = name.split(" ")
#Say hello to the User
print(f"Hello, {name}")
print(f"My first name is {first}")
print(f"My middle name is {middle}")
print(f"My last name is {last}")
# print(*objects , sep = ' ' , end = '\n' , file= sys.stdout , flush=False)

#Puesdocode for this code is 
#Multiple Comments for the line 
"""
#Ask user for thier name 

#Say hello to the user 
"""