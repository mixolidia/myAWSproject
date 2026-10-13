# Working with Loops_1
import random # ex.2
# ex.1
print("Welcome to Guess the Number!")
print("The rules are simple. I will thin of a number, and you will try to guess it.")

# ex.2
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. Thsi si  correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn't it. Try again.".format(guess))