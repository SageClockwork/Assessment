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


rounds = ""
while rounds != "xxx":
    rounds = int_check("How many questions would you like (<enter> for infinite)?: ", exit_code="xxx", infinite="")
    if rounds == "":
        print("You chose infinite mode")
    else:
        print(f"You asked for {rounds}")
            



