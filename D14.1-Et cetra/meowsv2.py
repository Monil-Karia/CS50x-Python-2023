def meow(n: int) -> None: #This means that we return None as return value 
    for _ in range(n):
        print("Meow_v1")

def meow_v2(n: int) -> str: #This means that we return string as a return value 

    ''' 
    Hello this is Doc string
 
    :param n: Number of times to meow
    :type n: int
    :raise TypeError: if n is not in an int
    :return : A String of n mewos, one per line 
    :rtype: str
    '''
    return "meow_v2\n" * n

num: int = int(input("Number: "))    #num :int it shows that the
meows1: str = meow(num)
meows2: str = meow_v2(num)
print(meows1)
print(meows2 , end="")