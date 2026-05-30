import random
import pyfiglet
import sys


font_list = pyfiglet.FigletFont.getFonts()

if len(sys.argv) == 1:
    inp = input("Input: ")
    font = random.choice(font_list)
    text = pyfiglet.figlet_format(inp, font=font)
    print("Output: " + text)


elif (
    len(sys.argv) == 3
    and (sys.argv[1] == "-f" or sys.argv[1] == "--font")
    and sys.argv[2] in font_list
):
    inp = input("Input: ")
    text = pyfiglet.figlet_format(inp, font=sys.argv[2])
    print("Output: " + text)

else:
    sys.exit("Error")
