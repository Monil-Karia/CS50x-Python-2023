#Must watch video for debuggin on youtube
# Watch any latest video for it no such preferences :)
def main():
    height = int(input("Height?: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * (i+1))

if __name__ == "__main__":
    main()