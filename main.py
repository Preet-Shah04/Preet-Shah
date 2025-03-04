# Making computer to select Rock, Paper or Scissors 

import random
opponent=random.choice(["R","P","S"])

# Displaying menu for user to Select his choice

print("Select 'R' for Rock")
print("Select 'P' for Paper")
print("Select 'S' for Scissors")

# Taking input of choice from user

a = input("Enter your choice: ")

# Making it upper case so that there is no typing issue

a = a.upper()

# Declaring dictionary for accessing user input

game_dictionary={"R":"Rock", "P":"Paper", "S":"Scissors"}

# Valid user input

if a not in game_dictionary:
    print("Invalid choice!\nChose from R or P or S")
else:
    # Displaying users choice

    print("You chose: ",game_dictionary.get(a))

    # Displaying opponents(computer's) choice

    print("Your opponent chose:",game_dictionary.get(opponent))


# Using if-else leader to decide winner,looser or match is draw

    if(opponent==a):
        print("It's a Draw!\nRematch")
    else:
        if(opponent=="R" and a=="S"):
            print("You Lose!\nRock broke the Scissors\nRetry")
        elif(opponent=="R" and a=="P"):
            print("Congratulations!\nYou win!\nPaper covers the Rock")
        elif(opponent=="P" and a=="R"):
            print("You Lose!\nPaper covers the Rock\nRetry")
        elif(opponent=="P" and a=="S"):
            print("Congratulations!\nYou win!\nScissors are sharp to cut the Paper")
        elif(opponent=="S" and a=="R"):
            print("Congratulations!\nYou win!\nRock broke the Scissors")
        elif(opponent=="S" and a=="P"):
            print("You Lose!\nScissors are sharp to cut the Paper\nRetry")
        else:
            print("Something went wrong Try again")

