from random import randint

player_lives = 5
computer_lives = 5

#  storing weapons in an array
choices = ["Rock", "Paper", "Scissors"]
player = False

#randomly picking one item
computer = choices[randint(0, 2)]

# define a win or lose function instead of the procedual way
def winorlose(status):
    # handle win or lose based on the status we pass in
    print("Called the win or lose function")
    print("==============")
    print("You", status, "!", "would you like to play again?")
    choice = input("Y / N:")

    if choice == "Y" or choice == "y":
        # reset the game
        # change global variables
        global player_lives
        global computer_lives
        global player
        global computer


        player_lives = 5
        computer_lives = 5
        player = False
        computer = choices[randint(0, 2)]
    elif choice == "N" or choice == "n":
        print("You chose to quit")
        exit()


# set up our loop
while player is False:
    print("=============================")
    print("Player Lives:", player_lives, "/5")
    print("AI Lives:", computer_lives, "/5")
    print("=============================")
    print("Choose your weapon! \n")
    player = input("Rock, Paper or Scissors? \n")


    # check to compare that same item has not been picked before
    if (player == computer):
        print("Tie! You live to shoot another day")
    elif player == "Rock":
        if computer == "Paper":
            # computer won
            player_lives = player_lives - 1
            print("You lose", computer, "covers", player, "\n")
            # if we won computer will loose life
        else:
            computer_lives = computer_lives - 1
            print("You win!", player, "smashes", computer, "\n")

    elif player == "Paper":
        if computer == "Scissors":
            #if player has selected paper and computer selected scissors, player will be defeated.
            player_lives = player_lives - 1
            print("You lose!", computer, "cuts", player, "\n")
            # vice versa 
        else:
            computer_lives = computer_lives - 1
            print("You win!", player, "covers", computer, "\n")

    elif player == "Scissors":
        if computer == "Rock":
            #if player choose scissors and computer chooses rock, rock will smash scissors so, 
            #player gets defeated by computer
            player_lives = player_lives -1
            print("You lose!", computer, "smashes", player, "\n")

        else:
            #as computer lost all its lifes,so we won , yayyyy
            computer_lives = computer_lives -1
            print("You win!", player, "cuts", computer, "\n")

    elif player == "quit":
        exit()

    else:
        #choice that is being made, is not from the available choices
        print("Check your spelling... that's not a valid choise!\n")
    
    if player_lives is 0:
        winorlose("lost")

    elif computer_lives is 0:
        winorlose("won")

    player = False 
    computer_choice = choices[randint(0, 2)]

