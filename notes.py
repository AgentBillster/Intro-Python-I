####################################################################
# 1. IF ELSE EXERCISE
# simply checks to see if User inputs pounds or kilos and respectively converts both units


def t1():
    weight = int(input("how fat u is? "))
    unit = input("(K)g or (L)bs ")
    if unit.upper() == "L":
        converted = weight * 0.45
        print(f"you are {converted} Kilos")
    else:
        converted = weight / 0.45
        print(f"you are {converted} Pounds")


####################################################################
# 2. WHILE EXERCISE
# i init some variables to help the game know what to do,
# as long as the lives arent at 0 the program will continue looping
def t2():
    lives = 5
    secret = 6
    while lives > 0:
        guess = int(input("Guess "))
        if guess != secret:
            lives -= 1
            print(f"{lives} lives left")
        else:
            print("correct!")
            break
    else:
        print("game over bitch")


####################################################################
    # ANOTHER THING FOR LOOP PRACTICE
def t3():
    command = ""
    is_started = False

    print("""
    commands:
    start - to start the car
    stop - to stop the car
    quit - to quit the game
        """)

    while True:
        command = input(">").lower()
        if command == "start":
            if is_started:
                print("car already started")
            else:
                is_started = True
                print("starting car...")

        elif command == "stop":
            if not is_started:
                print("car already stopped")
            else:
                is_started = False
                print("car stopped")
        elif command == "quit":
            break

        else:
            print("idk what that means")

####################################################################
    # the array represents how many x's to print per line to form letters


def t4():
    o = [5, 2, 5, 2, 2] # makes F
    l = [2, 2, 2, 6, 6] # makes L
    for i in o:
        output = ""
        for count in range(i):
            output += "x"
            print(output)
    

        
