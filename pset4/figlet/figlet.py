import sys
import random
from pyfiglet import Figlet

# Initialise class
figlet = Figlet()
fonts = figlet.getFonts()


# Check arguments inputs & font selected
if len(sys.argv) == 1:
    # Random choice selected
    f = random.choice(fonts)
elif len(sys.argv) != 3:
    sys.exit("Invalid usage")
else:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")

    if sys.argv[2] not in fonts:
        sys.exit("Invalid usage")

    f = sys.argv[2]
    
s = input("Input: ")
figlet.setFont(font=f)

print(figlet.renderText(s))
