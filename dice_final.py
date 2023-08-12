import random

# declared variables
i = 0
temp_num = ''
new_num = 0
dice = ''


# number generator per each dice option
def ran_num_2():
    return random.randint(1, 2)

def ran_num_4():
    return random.randint(1, 4)

def ran_num_6():
    return random.randint(1, 6)

def ran_num_8():
    return random.randint(1, 8)

def ran_num_10():
    return random.randint(1, 10)

def ran_num_12():
    return random.randint(1, 12)

def ran_num_20():
    return random.randint(1, 20)

def ran_num_100():
    return random.randint(1, 100)


# initial prompt
times = input("      How many dice? ")


while True:
    # ends program
    if times == "end":
        break

    else:
        try:
            # attempt to make input an int
            times = int(times)

            # if input is over a million it reprompts
            if(times > 1000000):
                print('')
                print("Haha nah, trust me...")
                print('')
                times = input("      How many dice? ")

            else:
                # prompts for the type of die
                dice = input("      What sided die? d")
                print('')
                # convers to int
                dice = int(dice)


                # rolling numbers
                while i < times:

                    # d2
                    if(dice == 2):
                        temp_num = ran_num_2()
                        print("Roll: ", temp_num)
                        new_num = temp_num + new_num
                        i += 1

                    # d4
                    elif(dice == 4):
                        temp_num = ran_num_4()
                        print("Roll: ", temp_num)
                        new_num = temp_num + new_num
                        i += 1

                    # d6
                    elif(dice == 6):
                        temp_num = ran_num_6()
                        print("Roll: ", temp_num)
                        new_num = temp_num + new_num
                        i += 1

                    # d8
                    elif(dice == 8):
                        temp_num = ran_num_8()
                        print("Roll: ", temp_num)
                        new_num = temp_num + new_num
                        i += 1

                    # d10
                    elif(dice == 10):
                        temp_num = ran_num_10()
                        print("Roll: ", temp_num)
                        new_num = temp_num + new_num
                        i += 1

                    # d12
                    elif(dice == 12):
                        temp_num = ran_num_12()
                        print("Roll: ", temp_num)
                        new_num = temp_num + new_num
                        i += 1

                    # d20
                    elif(dice == 20):
                        temp_num = ran_num_20()
                        print("Roll: ", temp_num)
                        new_num = temp_num + new_num
                        i += 1

                    # d100
                    elif(dice == 100):
                        temp_num = ran_num_100()
                        print("Roll: ", temp_num)
                        new_num = temp_num + new_num
                        i += 1

                    # reprompts if invalid dice type
                    else:
                        print("Enter a valid dice type: 2, 4, 6, 8, 10, 12, 20, 100")
                        break

                # prints total
                print('')
                print("Total: ", new_num)
                print('')
                # resets values
                i = 0
                new_num = 0
                # reprompts for number of dice
                times = input("      How many rolls? ")

        # reprompts incase of accidental inputs
        except:
            print('')
            print("Error")
            print('')
            times = input("      How many dice? ")