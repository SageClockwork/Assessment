import random


def yes_no(question):

    """Checks user responses to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # check the user says / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")

def instructions():
    
    """Prints instructions"""

    print("""
                 *** Instructions ***
          
Welcome to the Math Quiz!

Start by choosing the amount of questions / rounds you
want to answer ({enter} for infinite mode).

Next, you are going to choose the difficulty that you 
want to play at. Then, you will get a series of math 
questions to answer. The answers will be rounded to the 
closest integer.
          
 Good Luck.
          
    """)

def int_check(question, infinite=""): 
    
    # Checks if the user chooses a valid amount of rounds / questions.
    while True:
        response = input(question).lower()


        if response == infinite:
            return response
        
        if response<"1":
            error =  f"Please enter an integer that is more than / equals to 1"
        
        elif response != int:
            error = "Please enter an integer"

        try:
            response = int(response)

            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)

def answer_checker(question, exit_code=None ):
        
        
    # Checks if the user input is an integer.
    while True:
        response = input(question).lower()

        if response == exit_code:
            return response
        
        try:
            integer = int(response)
            return integer
        except ValueError:
            print("Please enter an integer")

def difficulty(question):
    """Checks if the user response to the question is hard / easy / mixed and returns their choice """

    while True:

        response = input(question).lower()

        # checks what difficulty the user asks for
        if response == "hard" or response == "h":
            return "hard"
        elif response == "easy" or response == "e":
            return "easy"
        elif response == "mixed" or response == "m":
            return "mixed"
        else:
            print("please enter e(easy) / h(hard) / m(mixed)")


# Variables
symbol_list = []
rounds_played = 0
mode = "regular"
statistics = ""
game_history = []
correct_answer = 0
incorrect_answer = 0
end_game= "no"

# Main routine...
# Display game name
print()
print("🔢 🔢 🔢 Welcome to the Math Quiz 🔢 🔢 🔢")
print()

# ask the user if they want instructions (check they say yes / no)
print()
want_instructions = yes_no("Do you want to see the instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

# Asks user how many rounds they want.
print()
rounds = int_check("How many questions would you like (<enter> for infinite)?: ", infinite="")

# Checks if infinite mode is chosen.
if rounds == "":
    mode = "infinite"
    rounds = 5

# Asks the user what difficulty they want.
print()
want_difficulty = difficulty("What difficulty do you want? ")

# Sets the symbols and attempts that will be used depending on user choice.
if want_difficulty == "easy":
    symbol_list = "+", "-"
elif want_difficulty == "hard":
    symbol_list = "*", "/"
else:
    symbol_list = "*", "/", "+", "-"

# Round loop starts here
while rounds > rounds_played and end_game == "no":

    # Round heading
    if mode == "infinite":
        print(f"=== Round {rounds_played+1} (infinite mode) ===")
    else:
        print(f"=== Round {rounds_played+1} ===")

    # Chooses a random symbol from the list and generates 2 random numbers.
    random_symbol = random.choice(symbol_list)
    num1 = random.randint(-100, 100)
    num2 = random.randint(-100, 100)
    

    # Finds the answer to the generated question
    if random_symbol == "+":
        answer = (num1 + num2)
    elif random_symbol == "-":
        answer = (num1 - num2)
    elif random_symbol == "*":
        answer = (num1 * num2)
    elif random_symbol == "/":
        answer = (num1 / num2)

    # Rounds the answer up to the nearest full integer
    answer = round(answer, 0)

    # Uses the random numbers and symbol to generate question
    print()
    print(answer)
    response = answer_checker(f"{num1} {random_symbol} {num2} = ", exit_code="xxx")

    # Checks if exit code is enters and ends game
    if response == "xxx":
        end_game= "yes"
        break
    
    # Rounds the user input up to the nearest full integer
    response = round(response, 0)

    # Gives the feedback of the round and saves the feedback
    if response == answer:
        feedback = "Correct!"
        print(feedback)
        correct_answer += 1

    else:
        feedback = "Wrong!"
        print("Wrong answer!")
        incorrect_answer += 1

    # Saves the question in game history and the user's answer
    history_item = f"Round: {rounds_played+1} Q:{num1} {random_symbol} {num2} = {response} (correct answer = {answer}, feedback = {feedback})"
    game_history.append(history_item)
    print()

    # Adds another round each time if mode is infinite.
    if mode == "infinite":
        rounds += 1
        
    # Adds another round to the rounds played variable
    rounds_played += 1

    

# Round loop ends here
    
# makes the statistics
statistics = f"""
    ----Statistics----

Questions answered: {rounds_played}
Correct answers: {correct_answer}
Wrong answers: {incorrect_answer}
Correct answer rate: {round(correct_answer/rounds_played*100)}%

""" 
# prints the statistics
print()
print(statistics)

# asks user if they want to see the game history
want_history = yes_no("Do you want to see the game history? ")

# prints the game history if response is yes
if want_history == "yes":
    print(f"\n{game_history}")

print()    
    


