from components import vars

def total(value):
    if value == 0:
        vars.character = vars.characters[0]

        print("It's " + vars.character)
       
    elif value <= 10:
        vars.character = vars.characters[1]

        print("It's " + vars.character)

    elif value <= 500:
        vars.character = vars.characters[2]

        print("It's " + vars.character)

    elif value <= 1000:
        vars.character = vars.characters[3]

        print("It's " + vars.character)

    else:
        vars.character = vars.characters[4]

        print("It's " + vars.character)
        