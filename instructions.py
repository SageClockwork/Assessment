 #functions go here

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




# Main routine
# Display game name
print()
print("\t🔢🔢🔢Welcome to the Math Quiz🔢🔢🔢")
print()

# ask the user if they want instrunctions (check they say yes / no)

want_instructions = yes_no("Do you want to see the instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    print("yes")

else:
    print("no")

