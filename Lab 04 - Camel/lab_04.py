import random


def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and outrun the natives.")
    user_choice = input("Press A to continue! ")
    if user_choice.upper() == "A":
        done = True

    # variables
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    natives = -20
    canteen = 3
    oasis = 0

    # Boolean while loop for options
    done = False
    while not done:
        print("A. Drink from your canteen. ")
        print("B. Ahead moderate speed. ")
        print("C. Ahead full speed. ")
        print("D. Stop for the night. ")
        print("E. Status check. ")
        print("Q. Quit. ")
        user_choice = input("How shall you choose your destiny? ")
        if user_choice.upper() == "Q":
            done = True
            print("You have sacrificed yourself to the natives!")
            print("Try again if you dare!")

        # Checking Status
        elif not done and user_choice.upper() == "E":
            print("Miles you have traveled ", miles_traveled)
            print("Number of drinks left in your canteen ", canteen)
            print("How many miles the natives are behind you ", miles_traveled - natives)

        # Stopping for the night
        elif not done and user_choice.upper() == "D":
            camel_tiredness = 0
            print("Your camel is feeling wonderful and is pleased with you!")
            natives += random.randrange(7, 15)

        # Full speed ahead
        elif not done and user_choice.upper() == "C":
            miles_traveled += random.randrange(10, 21)
            print("You have traveled", miles_traveled)
            thirst += 1
            camel_tiredness += random.randrange(1, 4)
            natives += random.randrange(7, 15)

        # Moderate speed ahead
        elif not done and user_choice.upper() == "B":
            miles_traveled += random.randrange(5, 13)
            print("Miles you have traveled ", miles_traveled)
            thirst += 1
            camel_tiredness += 1
            natives += random.randrange(7, 15)

        # Winning the game
        if miles_traveled >= 200:
            print("Congratulations you just won the game!")
            done = True

        # Drinking from the canteen
        elif not done and user_choice.upper() == "A":
            if canteen < 1:
                print("You were greedy and have ran out of water in the desert!")
            else:
                canteen -= 1
                thirst *= 0
                print("You are feeling refreshed, keep riding along!")

        # If your thirst got to high
        if thirst >= 6:
            print("You managed to dry your body of fluids! Oh well, you DIED!")
            done = True
        elif not done and thirst >= 4:
            print("You are thirsty!")

        # Camel is getting tired
        if camel_tiredness >= 8:
            print("Your camel is a broken animal, it has DIED!")
            done = True
        elif not done and camel_tiredness >= 5:
            print("Your pour camel is getting tired, you should rest it!")

        # How far back the natives are from you
        if miles_traveled - natives <= 0:
            print("The natives really want back their camel and have caught up to you. You just lost the game!")
            done = True
        elif not done and miles_traveled - natives <= 15:
            print("The natives are really close to capturing you, hurry up!")

        # Chance of finding an oasis
        if oasis == 20:
            camel_tiredness = 0
            thirst = 0
            canteen = 3
            print("Oh look at this...it appears you have found an oasis and have restored your stats!")


main()