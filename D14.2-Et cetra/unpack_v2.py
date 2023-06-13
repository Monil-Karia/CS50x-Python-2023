def f(*args , **kwargs):
    print("Positional: ",args , end = " ")
    print("Named: ", kwargs )


f(100,50,25)
f(galleons=100,sickels=50,knuts=25)