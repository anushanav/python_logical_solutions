# Guessing game between 1 to 8 in 5 chances

import random
def guess_number(guess):
    x = random.randint(1,8)
    chances =0
    while chances <4:
        if guess == x:
           print ("You guessed it correct.Congo!!")
           break
        else :
           print ("Wrong Guess.Sorry")
        chances += 1
        guess = int(input("guess the number "))
guess = int(input("guess the number "))
guess_number(guess)