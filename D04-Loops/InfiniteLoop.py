#we have induced a infinite loop while truew beacuse its always true and it alaways gonna run  
while True:
    n = int(input("What the n? "))
    if n>0:
        break    # used to escape the loop if the condition is true

for _ in range(n):
    print("Meow")

##Defiining the Function here
def main():
    n = get_number()
    meow(n)


def get_number():
    while True:
        n = int(input("Whats n? "))
        if n > 0:
            break
    return n     #Careful of the return where to indundate it program 


def meow(n):
    for i in range(n):
        print("Meow")

main()