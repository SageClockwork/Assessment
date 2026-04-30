import random 
#functions go here

def answer_checker(question, exit_code="xxx"):
    # Checks if the user input is an integer.
    while True:
        response = input(question)

        if response == exit_code:
            return response
        try:
            integer = int(response)
            return integer
        except ValueError:
            print("Please enter an integer")

response = ""
while response != "xxx":
    # Variables
    symbol_list = ["+", "-", "/", "*" ]
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

    # Rounds the answer and the user input up to the nearest full integer
    answer = round(answer, 0)
    # Asks the user the randomly generated question
    print(answer)
    response = answer_checker(f"{num1} {random_symbol} {num2} = ")
    response = round(response, 0)




    while response != answer:
        print("wrong answer")
        response = answer_checker(f"{num1} {random_symbol} {num2} = ")
        response = round(response, 0)

    print(f"Correct!")



        

