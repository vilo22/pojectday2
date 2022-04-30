# creatinga game
# allows user 7 chances to guess word
# if they do not guess after 7 tries
# the lost-program prints correct word and game ends
# other wise player wins and game ends

import random


# how do you make 7 chances happen?
# options - while loop, (count = 0 count += 1), if statement
# Instructions
# 1.  make a list of 10 words
# display the underscores
# keep track of the turns
# make a function that does step number 2
# 2. select a word from random list (this will be secret word aka answer)
# 3. secret word = "_______" ---- maybe every word is 5 characters, each character replaces an underscore .replace()///
# or possibly use len method to convert each character to an underscore
# what happens if they loose?
# what happens if they win?


# first, let's make a display


list_of_words = ['Event', 'Field', 'House', 'Japan', 'March', 'Owner',
                 'Controller', 'Television', "Description", 'Parangaricutirimicuaro']

secret_word = random.choice(list_of_words)


print("guess the characters")

guesses = " "

turns = 7

while turns > 0:
    failed = 0
    for letter in secret_word:
        if letter.lower() in guesses:
            print(letter)
            
        else:
            print('_')

            failed += 1
    if failed == 0:
        print("You Win")

        print("Correct! the word is: ", secret_word)
        break

    guess = input("Guess the letter:")

    guesses += guess

    if guess not in secret_word:
        turns -= 1
        print("Please try again")
        print("You have ", + turns, 'more guesses')

        if turns == 0:
            print("You Loose :-(")
