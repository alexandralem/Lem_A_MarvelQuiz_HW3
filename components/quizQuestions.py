from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)

questions = {
    "q1" : {
        "question": Fore.RED + "\033[1m" + "Were you born on Earth? " + "\033[0m",
        "yes" : 0,
        "no" : 500
    },

    "q2" : {
        "question": Fore.RED + "\033[1m" + "Do you have superpowers? " + "\033[0m",
        "yes" : 0,
        "no" : 2000
    },

     "q3" : {
        "question": Fore.RED + "\033[1m" + "Are you female? " + "\033[0m",
        "yes" : 3000,
        "no" : 0
    },

     "q4" : {
        "question": Fore.RED + "\033[1m" + "Can you fly? " + "\033[0m",
        "yes" : 50,
        "no" : 0
    },

     "q5" : {
        "question": Fore.RED + "\033[1m" + "Do you rely on specific weapons or any other items in battle? " + "\033[0m",
        "yes" : 100,
        "no" : 0
    },

    #Born on Earth: Hulk, Captain America, Hawkeye, Captain Marvel
    #Have superpowers: Hulk, Captain America, Thor, Captain Marvel
    #Female: Captain Marvel
    #Can fly: Thor, Captain Marvel
    #Carrries weapon: Captain America, Hawkeye, Thor

}