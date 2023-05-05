def main():
    text = input("Enter text: ")
    print(shorten(text))


def shorten(word):

    vowels = "aeiouAEIOU"

    ans = ""
    for char in word:
        if char not in vowels:
            ans += char
    return ans.lower()

if __name__ == "__main__":
    main()