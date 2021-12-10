from components import vars
from PIL import Image

def total(value):
    if value == 0:
        vars.character = vars.characters[0]

        print("It's " + vars.character)
        vars.images[0] = Image.open("images/hulk.jpg")
        vars.images[0].show()
       
    elif value <= 10:
        vars.character = vars.characters[1]

        print("It's " + vars.character)
        vars.images[1] = Image.open("images/captain.jpg")
        vars.images[1].show()

    elif value <= 500:
        vars.character = vars.characters[2]

        print("It's " + vars.character)
        vars.images[2] = Image.open("images/hawkeye.jpg")
        vars.images[2].show()

    elif value <= 1000:
        vars.character = vars.characters[3]

        print("It's " + vars.character)
        vars.images[3] = Image.open("images/thor.jpg")
        vars.images[3].show()

    else:
        vars.character = vars.characters[4]

        print("It's " + vars.character)
        vars.images[4] = Image.open("images/marvel.jpg")
        vars.images[4].show()
        