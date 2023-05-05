def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not condition1(s):
        return False
    if not condition2(s):
        return False
    if not condition3a(s):
        return False
    if not condition3b(s):
        return False
    if not condition4(s):
        return False
    return True

def condition1(s):
    return s[:2].isalpha()

def condition2(s):
    if(len(s) < 2 or len(s) > 6):
        return False
    return True 

def condition3a(s):
    if(s[-1].isalpha()):
        for char in s:
            if(char.isdigit()):
                return False
    return True


def condition3b(s):
    if s[0] == '0':
        return False
    return True

def condition4(s):
    if not s.isalnum():
        return False 
    return True

if __name__ == "__main__":
    main()