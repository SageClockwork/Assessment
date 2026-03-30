import random 
#functions go here
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


# Main routine
            
symbol_list = []

# ask the user what difficulty they want
print()
want_difficulty = difficulty("Difficulty (hard / easy / mixed): ")
# chooses the symbols according to the difficulty

if want_difficulty == "easy":
    symbol_list = ["+", "-"]
    random_symbol = random.choice(symbol_list)

elif want_difficulty == "hard":
    symbol_list = ["/", "*"]
  
else:
    symbol_list = ["/", "*", "+", "-"]

while True:
    random_symbol = random.choice(symbol_list)
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    # Asks the user the randomly generated question
    response = answer_checker(f"{num1} {random_symbol} {num2} = ")

    # Finds the answer to the generated question
    if random_symbol == "+":
        answer = (num1 + num2)
    elif random_symbol == "-":
        answer = (num1 - num2)
    elif random_symbol == "*":
        answer = (num1 * num2)
    elif random_symbol == "/":
        answer = (num1 / num2)

    # Rounds the answer and the user input up to the nearest full integer
    response = round(response, 2)
    answer = round(answer, 2)



    while response != answer:
        print("wrong answer")
        response = answer_checker(f"{num1} {random_symbol} {num2} = ")
        response = round(response, 2)

    print(f"Correct!")




