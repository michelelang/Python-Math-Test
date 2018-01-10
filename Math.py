from random import randint, choice

result_dict = {

}
INCORRECT = 0
CORRECT = 0

def generate_math_problem():
    num1 = randint(1, 100)
    num2 = randint(1,100)
    ops = choice(['+', '-', '*'])
    math_problem = (str(num1) + " " + str(ops) + " " + str(num2))
    math_problem_printed = (str(num1) + " " + str(ops) + " " + str(num2) + " = ")
    get_user_answer(math_problem, math_problem_printed)
    return math_problem, math_problem_printed

def get_user_answer(math_problem, math_problem_printed):
    user_input = int(raw_input(math_problem_printed))
    validate_answer = eval(math_problem)
    validate_answer_func(validate_answer, user_input, math_problem)
    return user_input

def validate_answer_func(validate_answer, user_input, math_problem):

    if user_input == validate_answer:
        print "Yay, correct!"
        global CORRECT
        CORRECT += 1
    else:
        print "Incorrect"
        global INCORRECT
        INCORRECT += 1
        result_dict[math_problem] = "your answer: " + str(user_input), "correct answer: " + str(validate_answer)
    return result_dict

def success_rate():
    global INCORRECT
    global CORRECT
    total = INCORRECT + CORRECT
    percentage = int(100 * (float(CORRECT)/total))
    print "You answered " + str(CORRECT) + " correct and " + str(INCORRECT) + " incorrect, out of " + str(total) + " questions. " + str(percentage) + "%"

def play_again():
    playAgain = True
    while (playAgain):
        generate_math_problem()
        play = str(raw_input("Do you want to play again?"))
        if play == "no" or play == "No" or play == "n" or play == "N":
            playAgain = False
            success_rate()
            global INCORRECT
            if INCORRECT > 0:
                print "Incorrect problems and answers: "
                print result_dict
        else:
            playAgain = True


play_again()




