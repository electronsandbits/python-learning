def find_time(str):
    """
    takes in a string and, if it contains one, returns a time written in the string.
    Times will be of the format "XX:XX" and you don't need to include any AM or PM designations.

    >>> find_time("Let's go to the movies at 09:30 tomorrow")
    '09:30'
    """
    pass


def parse_out_hashtag(s):
    """
    This function takes in a string representing a single tweet and returns a list of all hashtags in the tweet.

    >>> parse_out_hashtag('I am going to #wearmymask everywhere')
    'wearmymask'

    >>> parse_out_hashtags('what is #ResX?')
    'ResX'
    """
    pass


def find_price(line, currency):
    """
    We want to look through a line and find the place where a price is mentioned.
    You can assume that the currency symbol specified will only show up once in
    the line provided.
    To find the price, locate the currency symbol and then find all the digits AFTER
    the symbol (not all currencies have the symbol come first--think about how
    we could adjust our code if the symbol came last, instead). Stop reading once the
    last digit has been read. Return the price as an integer (without the currency
    symbol).
    >>> find_price('Une cramique au chocolat coûte €3', '€')
    3
    """
    pass

def exclaim_word(s):
    """
    This function takes in a string and returns a list of the exclamatory words in that string.
    Consider an exclamatory word the "word" substring of one or more alphabetic chars
    which are immediately to the left of the '!' in s.

    >>> exclaim_word('x123hello!cs106a')
    'hello'

    >>> exclaim_word('32happy!day')
    'happy'
    """
    pass

def parse_username(s):
    """
    Takes in a string s representing an email address, and returns the username.

    >>> parse_username('maya.angelou1@gmail.com')
    'maya.angelou1'
    """
    pass


def parse_hostname(s):
    """
    Takes in a string representing an email address, and returns the host name

    >>> parse_hostname('nick@cs.stanford.edu')
    'cs.stanford.edu'
    """
    pass


def parse_phone_number(s):
    """
    This function uses a while loop accompanied with str.find() to parse a phone number into a list of strings
    where the first string is the area code of the given phone number and the second string is the rest of
    the phone number with the dash characters removed. This function will work for all phone numbers,
    not just 10 digit ones.

    >>> parse_phone_number('Zoom is too much-call me instead: 212-225-9876')
    ['212', '2259876']

    >>> parse_phone_number('so call-me beep-me if you wanna reach me-at 650-555-5555')
    ['650', '5555555']
    """
    pass

def main():
    # Add code here to test the functions
    pass

if __name__ == "__main__":
    main()