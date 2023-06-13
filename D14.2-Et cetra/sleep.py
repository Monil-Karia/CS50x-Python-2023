def main(): 
    n = int(input("what's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "Sheep" * i 
    # flock = []
    # for i in range(n):
    #     flock.append("Sheep"*i)
    # return flock

if __name__ =="__main__":
    main()