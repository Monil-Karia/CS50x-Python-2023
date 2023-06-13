from hello import hello

def test_default():
    #This will not run because it is not returning any value 
    # hello("David") == "hello, David"
    hello() == "hello, world"

def test_argument():
    #When we modify the design of the program then it usable for the testing
    hello("David") == "hello, David"