from components import vars
from PIL import Image
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)

def total(value):
    if value <= 10:
        vars.character = vars.characters[0]

        print(Fore.GREEN + "\033[1m" + "It's " + vars.character + "\033[0m")
        vars.images[0] = Image.open("images/hulk.jpg")
        vars.images[0].show()
       
    elif value <= 100:
        vars.character = vars.characters[1]

        print(Fore.GREEN + "\033[1m" + "It's " + vars.character + "\033[0m")
        vars.images[1] = Image.open("images/captain.jpg")
        vars.images[1].show()


    elif value <= 1000:
        vars.character = vars.characters[3]

        print(Fore.GREEN + "\033[1m" + "It's " + vars.character + "\033[0m")
        vars.images[3] = Image.open("images/thor.jpg")
        vars.images[3].show()

    elif value <= 2500:
        vars.character = vars.characters[2]

        print(Fore.GREEN + "\033[1m" + "It's " + vars.character + "\033[0m")
        vars.images[2] = Image.open("images/hawkeye.jpg")
        vars.images[2].show()

    else:
        vars.character = vars.characters[4]

        print(Fore.GREEN + "\033[1m" + "It's " + vars.character + "\033[0m")
        vars.images[4] = Image.open("images/marvel.jpg")
        vars.images[4].show()
