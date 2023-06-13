balance = 0 
def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n
    
def main():
    print("Balance:" ,balance)
    deposit(100)
    withdraw(50)
    print("Balance:" ,balance)


if __name__ == "__main__":
    main()