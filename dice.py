import random

# declares dice
dice = ''

# options for dice
valid_ans = {4, 6, 8, 10, 12, 20, 100}


while True:
    # askes for what type of die
    dice = input("      what sided die? d")

    # gives the option to end program
    if (dice == "end"):
        break

    # converts input to int
    try:
            dice = int(dice)

    # if it cant (str or char) it will restart program
    except:
        # isinstance(dice, str)
        print("error")

    else:
        # if value is not valid than restart program
        if dice not in valid_ans:
            print("error")

        # otherwise will produce a dice roll
        else:
            if(dice == 4):
                print(random.randint(1, 4))

            elif(dice == 6):
                print(random.randint(1, 6))

            elif(dice == 8):
                print(random.randint(1, 8))

            elif(dice == 10):
                print(random.randint(1, 10))

            elif(dice == 12):
                print(random.randint(1, 12))

            elif(dice == 20):
                print(random.randint(1, 20))

            elif(dice == 100):
                print(random.randint(1, 100))

            else:
                print("error")


# the program should work as intended