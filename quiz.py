from components.quizQuestions import questions
from components import vars, quizTally
from colorama import Fore, Back, Style
from colorama import init

init(autoreset=True)

print(Fore.BLUE + "\033[1m" + "Choose one of the following characters and keep this character in your mind while answering questions: Thor, Captain America, Hulk, Hawkeye, Captain Marvel" + "\033[0m")

answer1 = questions["q1"][input(questions["q1"]["question"])]
print(answer1)

vars.quizTotal += answer1
print("++++++++++++++++++++++++++++")

answer2 = questions["q2"][input(questions["q2"]["question"])]
print(answer2)

vars.quizTotal += answer2
print("++++++++++++++++++++++++++++")

answer3 = questions["q3"][input(questions["q3"]["question"])]
print(answer3)

vars.quizTotal += answer3
print("++++++++++++++++++++++++++++")

answer4 = questions["q4"][input(questions["q4"]["question"])]
print(answer4)

vars.quizTotal += answer4
print("++++++++++++++++++++++++++++")

answer5 = questions["q5"][input(questions["q5"]["question"])]
print(answer4)

vars.quizTotal += answer5
print("++++++++++++++++++++++++++++")


print("total so far: " + str(vars.quizTotal) + "\n")

quizTally.total(vars.quizTotal)
