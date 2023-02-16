# this programme demonstrates a guessing game
# gets user's input
user_name = input("What's your name?")
print("Hello there" + user_name + "!")

counter = 0
# generates a random number
from random import randint


# using a while loop
while counter <5:
    user_name = eval(input("Pick a number of your choice"))


# checks if user input is equal to random number