def wordguess_helper(guessed_word, secret_word, guess):
    """
    Write a function that helps us play wordguess.
​
    The user will pass in:
    guessed_word: what we've guessed so far in the word; unguessed letters represented by "-"
    secret_word: the word we are trying to guess
    guess: the letter we are guessing this round
​
    The function should return a new_guessed_word that represents our obscured word updated
    by the most recent guess. Make sure to build up a new string letter by letter!

    >>> wordguess_helper('------', 'Python', 'o')
    '----o-'
    """
    pass



def exclaim(msg, end, n):
    """
    Implements exclaim as specified in the handout
    """
    pass



def main():
    print("\nChecking solutions to Exclaim...\n")

    print("\n")
    print("Calling exclaim('Did you see the new Star Wars movie', '?!', 6)")
    exclaim('Did you see the new Star Wars movie', '?!', 6)
    print("Calling exclaim('106A is awesome', '!', 5)")
    exclaim('106A is awesome', '!', 5)



if __name__ == "__main__":
    main()