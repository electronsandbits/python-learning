"""
In a number-guessing game, where the computer
thinks of a number and the player is allowed several
guesses, there’s no need to keep asking the player
after they’ve guessed correctly.
"""
computers_number = 9
guessed_correct = False

# Player gets 5 guesses
for guesses in range(1, 6):
    players_number = input('Enter your guess> ')

    if computers_number == players_number:
        guessed_correct = True
        # Break out of the loop immediately because the player guessed correctly
    print('Try again!, guesses, left.')
    # At this point, player either guessed correctly or used up all guesses without  success.
message = 'You win!' if guessed_correct else 'You lose!'
print(message)
