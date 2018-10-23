from random import randint

#  available weapons => store this in an array
choises = ["Rock", "Paper", "Scissors"]
player = False

# make the computer pick one item at random
computer_choise = choises[randint(0, 2)]

# show the computer's cjoise in the terminal window
print("Computer chooses: ", computer_choise)

# set up our loop
while player is False:
	# set player to True by making a selection
	print("Choose your weapon!")
	player = input("Rock, Paper or Scissors?")

	print(player, "\n")

    # check for a tie = choices are the same
	if player == computer_choise:
	    print("Tie! You live to shoot another day")

	# check to see if the computer choise beats our choise or not
	elif player == "Rock":
		if computer_choise == "Paper":
			# computer won, crap!!
			print("You lose! Pager convers Rock")
	    else:
	    	# we win! such winning
	    	print("You win!", player "smashes", computer_choise)

    elif player == "Paper":
    	if computer_choise == "Scissors":
    		print("You lose!", computer_choise, "cut", player)
    	else:
    		print("You won!", player, "covers", computer_choise)

    elif player == "Scissors":
        if computer_choise == "Rock":
            print("You lose!", computer_choise, "smashes", player)
        else:
            print("You win!", player, "cut", computer_choise)
    elif player== "quit":
        exit()
        else:
            print("Check your spelling... that's not a valid choise\n")

    # reset the game loop and start over again
    player = False
    computer_choise = choises[radint(0,2)]    		

