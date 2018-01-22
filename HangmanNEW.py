import random
import turtle

wn = turtle.Screen()      
alex = turtle.Turtle()

easywords = ["scary", "plant", "money"]
random.shuffle(easywords)
targetword = easywords[0]
spacelist = list(easywords[0])
print(spacelist)
print("_ " * len(targetword))

guessed = len(targetword) * "_"
playing = True

while playing:
    guess = input("Guess a letter or the word (if you know it) !")
    if spacelist.__contains__(guess):
        print("good job!")
        spaces = list(guessed)
        print(spaces)
        replace = spacelist.index(guess)
        print(spacelist.index(guess))
        spaces[spacelist.index(guess)] = guess
        guessed = spaces
        print(spaces)
    elif guess == easywords[0]:
        print("THATS THE WORD! YOU WIN!")
        
    else:
        alex.circle(50)
        print ("Wrong, guess again!" ) 