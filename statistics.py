def int_check(question, exit_code=None, infinite=""): 
    
    # if any integer is allowed... 
    while True:
        response = input(question).lower()

        if response == exit_code:
            return response
        elif response == infinite:
            return response
        
        if response<"1":
            error = (f"Please enter an integer that is "
                     f"more than / equal to 1")
        
        elif response != int:
            error = (f"Please enter an integer")

        try:
            response = int(response)

            if response < 1:
                print(error)


            else:
                return response

        except ValueError:
            print(error)

rounds_played = 10

correct_answer = int_check("Correct: ")
incorrect_answer = int_check("Incorrect: ")

statistics = f"""
    ----Statistics----

Questions answered: {rounds_played}
Correct answers: {correct_answer}
Wrong answers: {incorrect_answer}
Correct answer percentage: {round(correct_answer/rounds_played*100)}
Wrong answer percentage: {round(incorrect_answer/rounds_played*100)}


""" 

print(statistics)