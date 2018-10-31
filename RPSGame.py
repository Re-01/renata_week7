from random import randint

#  storing weapons in an array
choices = ["Rock", "Paper", "Scissors"]
player = False

player_lives = 5
computer_lives = 5

#randomly picking one item
computer = choices[randint(0,2)]


# show the computer's choise in the terminal window
print("Computer chooses", computer)


# set up our loop
while player is False:
    # set player to True by making a selection
    print("Choose your weapon!")
    player = input("Rock, Paper or Scissors?")

    print(player, "\n")

    # check to compare that same item has not been picked before
if (player == computer):
    print("Tie! You live to shoot another day")
    #computer won. Check to see we are defeated by computer or not
elif player == "Rock":
    if computer == "Paper":
        # computer won
        player_lives = player_lives -1
        print("You lose", computer, "covers", player)
        # if we won computer will loose life
    else:
        computer_lives = computer_lives -1
        print("You win!", player, "smashes", computer)

elif player == "Paper":
    if computer == "Scissors":
        #if player has selected paper and computer selected scissors, player will be defeated.
        player_lives = player_lives -1
        print("You lose!", computer, "cuts", player)
        # vice versa 
    else:
        computer_lives = computer_lives -1
        print("You win!", player, "covers", computer)

elif player == "Scissors":
    if computer == "Rock":
        #if player choose scissors and computer chooses rock, rock will smash scissors so, 
        #player gets defeated by computer
        player_lives = player_lives -1
        print("You lose!", computer, "smashes", player)

    else:
        #as computer lost all its lifes,so we won , yayyyy
        computer_lives = computer_lives -1
        print("You win!", player, "cuts", computer)

elif player== "quit":
    exit()

else:
    #choice that is being made, is not from the available choices
    print("Check your spelling... that's not a valid choise!\n")

    #checking win/lose
    if player_lives is 0:
        print("You don't have any life, play again?")

        choice = input("Y / N? ")

        if choice == "Y" or choice == "y":
            player_lives = 5
            computer_lives = 5
            player = False
            computer = choices[randint(0,2)]
        elif choice == "N" or choice == "n":
            print("You've had enough losing")
            exit()

    if computer_lives is 0:
        print("Computer is out of lives! would you like to play again?")
        # taking to input from the user, if he want to play again
        choice = input("Y / N? ")

        # so if user chosen to play again, lets intialize the lives again
        if choice == "Y" or choice == "y":
            player_lives = 5
            computer_lives = 5
            player = False
            computer = choices[randint(0,2)]
    elif choice == "N" or choice == "n":
        print("You've had enough losing")
        exit()

    # reset the game loop and start over again
    player = False
    computer = choices[randint(0,2)]    