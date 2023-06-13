def main():
    yell("This" , "is", "CS50")

def yell(*words):
    uppercased = map(str.upper,words)
    uppercased_list = [word.upper() for word in words]
    print(*uppercased)
    print(*uppercased_list)


if __name__ == "__main__":
    main()