from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if sys.argv[1] == "-f" or sys.argv[1] == "--font":
    if len(sys.argv) == 1:
        input_text = input("Text: ")
        figlet.setFont(font=random.choice(figlet.getFonts()))
        print(figlet.renderText(input_text))

    elif len(sys.argv) == 3:
        input_text = input("Text: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(input_text))

else:
    sys.exit("Invalid Usage")
