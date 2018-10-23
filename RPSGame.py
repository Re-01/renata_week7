from random import randint

#  available weapons => store this in an array
choises = ["Rock", "Paper", "Scissors"]

# make the computer pick one item at random
computer_choise = choises[randint(0, 2)]

# show the computer's cjoise in the terminal window
print("Computer chooses: ", computer_choise)
