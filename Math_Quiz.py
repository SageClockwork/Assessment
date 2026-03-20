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

Start by choosing a difficulty (easy, medium, hard), which 
will make questions depending on the difficulty you chose.

Next, you are going to choose the amount of questions or 
rounds you want to play. Then, you will get a series of math 
questions to anser.
          
 Good Luck.
          
    """)

def int_check(question, low=None, high=None, exit_code=None, infinite=""): 
    
    # Checks if the user chooses a valind amount of rounds / questions.
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


#Main routine...
# Display game name
print()
print("🔢 🔢 🔢 Welcome to the Math Quiz 🔢 🔢 🔢")
print()

# ask the user if they want instrunctions (check they say yes / no)

want_instructions = yes_no("Do you want to see the instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()


# Asks user how many rounds they want.

rounds = int_check("How many questions would you like (<enter> for infinite)?: ", low=1, exit_code="xxx", infinite="")
    
            



