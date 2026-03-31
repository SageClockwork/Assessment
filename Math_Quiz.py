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

Start by choosing a difficulty (easy, hard, or mixed), which 
will make questions depending on the difficulty you chose.

Next, you are going to choose the amount of questions or 
rounds you want to play. Then, you will get a series of math 
questions to answer. The answers will always be rounded up.
          
 Good Luck.
          
    """)

def int_check(question, low=None, high=None, exit_code=None, infinite=""): 
    
    # Checks if the user chooses a valid amount of rounds / questions.
    while True:
        response = input(question).lower()

        if response == exit_code:
            return response
        elif response == infinite:
            return response
        
        if response<"1":
            error = (f"Please enter an integer that is "
                     f"more than / or equal to 1")
        
        elif response != int:
            error = (f"Please enter an integer")

        try:
            response = int(response)

            if low is not None and response < low:
                print(error)

            elif high is not None and response > high:
                print(error)

            else:
                return response

        except ValueError:
            print(error)

def answer_checker(question):
    # Checks if the user input is an integer.
    while True:
        response = input(question)
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
rounds = int_check("How many questions would you like (<enter> for infinite)?: ", low=1, exit_code="xxx", infinite="")

# Checks if infinite mode is chosen.
if rounds == "":
    mode = "infinite"
    rounds = 5

# Asks the user what difficulty they want.
print()
want_difficulty = difficulty("What difficulty do you want? ")

# Sets the symbols that will be used depending on user choice.
if want_difficulty == "easy":
    symbol_list = "+", "-"
elif want_difficulty == "hard":
    symbol_list = "*", "/"
else:
    symbol_list = "*", "/", "+", "-"

# Round loop starts here
while rounds > rounds_played:
    # Round heading
    if mode == "infinite":
        print(f"=== Round {rounds_played+1} (infinite mode) ===")

    else:
        print(f"=== Round {rounds_played+1} ===")

    # Chooses a random symbol from the list and generates 2 random numbers.
    random_symbol = random.choice(symbol_list)
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    # Finds the answer to the generated question
    if random_symbol == "+":
        answer = (num1 + num2)
    elif random_symbol == "-":
        answer = (num1 - num2)
    elif random_symbol == "*":
        answer = (num1 * num2)
    elif random_symbol == "/":
        answer = (num1 / num2)

    # Uses the random numbers and symbol to generate question
    print()
    print(answer)
    response = answer_checker(f"{num1} {random_symbol} {num2} = ")

    # Rounds the answer and the user input up to the nearest full integer
    response = round(response, 2)
    answer = round(answer, 2)


    # Tells the user if their answer is wrong and regenerates the same question and rounds the response again.
    while response != answer:
        print("wrong answer")
        print(answer)
        response = answer_checker(f"{num1} {random_symbol} {num2} = ")
        response = round(response, 2)

    # Tells user that their answer is correct.
    print(f"Correct!")
    rounds_played += 1

    # Adds another round each time if mode is infinite.
    if mode == "infinite":
        rounds += 1

# Round loop ends here