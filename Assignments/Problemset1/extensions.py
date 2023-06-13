input = input("Your file name? ")

if(input.endswith(".pdf")):
    print("application/pdf")
elif(input.endswith(".jpeg")):
    print("images/jpeg")
elif(input.endswith(".jpg")):
    print("images/jpg")    
elif(input.endswith(".gif")):
    print("images/gif")
elif(input.endswith(".png")):
    print("images/png")
elif(input.endswith(".txt")):
    print("application/txt")
elif(input.endswith(".zip")):
    print("application/zip")