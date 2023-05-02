name = input("What's your name? ")

# "w" is dangerous as it writes and erases the last written word
# "a" is appending 
#We can use "with" "as" keyywords for the c,osing and for anyoperation in the file
with open("names.txt" , "a") as file:
    file.write(f"{name}\n")


#Close is optional when you are using the file but a good pratcice
# file.close()
