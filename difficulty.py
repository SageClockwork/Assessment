import random 
#functions go here


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
want_difficulty = difficulty("What difficulty do you want? ")

# chooses the symbols according to the difficulty

if want_difficulty == "easy":
    symbols = "+", "-"
    symbol_list.append(symbols)

elif want_difficulty == "hard":
    symbols = "*", "/"
    symbol_list.append(symbols)
  
else:
    symbols = "*", "/", "+", "-"   
    symbol_list.append(symbols) 



print(f"{random.randint(0, 100)} {random(symbol_list)} {random.randint(0, 100)}"
      f"Answer:")



        

