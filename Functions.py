# let's explore some functions and how to write them
# and also what they do


def greeting():
    # say hello
    print("Hello from the greetings function")


# invoke or call the function
greeting()


def greetings(msg="hello there!", num=0):
    print("our function says", msg, "The second arg is", num)


greetings()
greetings("This is an argument", 1)
greetings("Why are we arguing?", 2)

myVariableNumber = 0


def someMath(num1=2, num2=5):
    global myVariableNumber

    myVariableNumber = num1 + num2
    return num1 + num2


sum = someMath()
print("Our sum variable is:", sum, "myVariableNumber is also", sum)

sum = someMath(10, 15)
print("another math operation with", sum, "as the result")
