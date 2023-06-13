text = input("Enter text: ")

vowels = "aeiouAEIOU"

new_text = ""
for char in text:
    if char not in vowels:
        new_text += char

print("Text with vowels removed: " + new_text)