import random

def parse_trades(filename):
    """
    This function takes in the name of a file containing
    trades for the NYSE stock Gamestop (GME) and prints
    the total number of shares bought and sold.
    """
    pass

def create_pylib(filename):
    """
    This function reads a PyLib from the given filename and prints out a completed story!
    """
    pass

#### We provided the following constant dictonary called words and the get_word function below. ####
#### You will be able to write this yourself in a few weeks.  #####
#### Feel free to look it over, but don't worry if it is confusing. It should be at this time. ####

WORDS = {"noun": ["coding project", "Zoom meeting", "pineapple", "face shield", "grilled cheese", "garden", "textbook"],
         "adjective": ["exciting", "sleepy", "energetic", "delicious", "difficult", "fun"],
         "verb": ["dance", "see", "borrow", "explain", "eat", "code", "learn"],
         "adverb": ["happily", "quickly", "hesitantly", "impulsively", "courageously", "angrily"],
         "verb ending in -ing": ["traveling", "quarantining", "coding", "learning", "ordering", "eating"],
         "location": ["Palo Alto", "Stanford", "CoHo", "Albuquerque, NM", "the Pacific Northwest", "Wilbur Dining"]
         }

def get_word(category):
    """
    Use get_word(category) to generate a random word from the category specified.
    We provided this code, but in just a few weeks you could write it yourself!
    ​
    Input: a string representing a word category
    Valid categories:
    - "noun"
    - "adjective"
    - "verb"
    - "adverb"
    - "verb ending in -ing"
    - "location"
    ​
    Output: a string representing a word from the specified category
    """
    if category in WORDS:
        return random.choice(WORDS[category])
    else:
        return "INVALID CATEGORY: " + category



if __name__ == "__main__":

    # This tests the first two functions in this file
    WORDS_FILE = "words.txt"
    print("Number of peaceful words in English language: " + str(count_peaceful(WORDS_FILE)))
    print("Number of stacatto words in English language: " + str(count_stacatto(WORDS_FILE)))

    # This tests the parse_trades function (should be 58 bought, 38 sold).
    GAME_STOP_FILE = "gamestop_trades_10.txt"
    parse_trades(GAME_STOP_FILE)

    # This tests the create_pylib function
    PYLIB_FILE = 'pylib.txt'
    create_pylib(PYLIB_FILE)

