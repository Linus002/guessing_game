# this programme demonstrates a guessing game
# gets user's input
player = input("What's your name?")
print("Hello there" + player + "!")

# generates a random number
from random import randint
number = randint(1, 100)

counter = 0


# using a while loop
while counter <5:
    user_number = eval(input("Enter a number:"))
    counter += 1

# checks if usernumber is equal to randomly generated number
    if user_number < number:
        print("Your guess is too low.") 
    elif user_number > number:
        print("Your guess is too high")
    elif user_number == number:
        print("Correct.You win")
        break


    