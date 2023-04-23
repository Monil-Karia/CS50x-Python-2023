import sys

#Error handling of Index error
# try:
#     
#     print("Hello my name is", sys.argv[1])
# except(IndexError):
#     print("Too few Errors")

##New concept 
#here 1 in sys.argv because sys.argv [0] has name of file we are interpreting   

#Check for errors
if len(sys.argv) < 2:
    sys.exit("Too few Arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many Arguments")

#Priting the name  
print("Hello , my Name is :" , sys.argv[1])

