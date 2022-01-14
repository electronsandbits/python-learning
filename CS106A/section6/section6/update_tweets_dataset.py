"""
Juliette wrote this to update the datasets to only have a single hashtag per line since we did not do
nested while loop string parsing in Spring 20-21 quarter.
"""


OLD_FILE = 'huge-tweets-old.txt'
FILE = 'huge-tweets.txt'

def main():
    for line in open(OLD_FILE):
        line = line.strip()
        tags = parse_tags(line)
        if len(tags) == 0:
            with open(FILE, 'a') as f:
                f.write(line + '\n')
        for tag in tags: # for each hashtag, make the tweet using only that hashtag
            new_tweet = update_line(line, tags, tag)
            with open(FILE, 'a') as f:
                f.write(new_tweet + '\n')


TEST = '@realDonaldTrump: RT @DonaldJTrumpJr: Great pic from a friend on @CBPflorida @CustomsBorder who have been helping with #harvey recovery and now with #irma. T…'
GUESS = '@realDonaldTrump: RT @IvankaTrump: This year’s #TaxDay is the last time you’ll have to file your taxes through an outdated, broken system. BYE-BYE https://t…'


def update_line(line, tags, tag):
    """
    >>> update_line('#juliette #python today is great', ['#juliette', '#python'], '#juliette')
    '#juliette python today is great'
    >>> update_line('#juliette #python today is great', ['#juliette', '#python'], '#python')
    'juliette #python today is great'
    >>> update_line(TEST, ['#harvey', '#irma'], '#harvey')
    GUESS
    """
    splits = line.split()
    new_tweet = ''
    for word in splits:
        num_tags_in_word = count_hash(word)
        if num_tags_in_word > 1:
            all_tags = word.split('#')[1:]
            all_tags = ['#' + tag for tag in all_tags]
            for mini_word in all_tags:
                if mini_word in tags and not mini_word.startswith(tag):
                    mini_word = mini_word[1:]
                new_tweet += mini_word
                new_tweet += ' '
        else:
            stripped_word = word.strip(',.?!/(){}')
            if stripped_word in tags and not word.startswith(tag):
                word = word[1:]
            new_tweet += word
            new_tweet += ' '
    return new_tweet.strip()


def count_hash(s):
    count = 0
    for ch in s:
        if ch == '#':
            count += 1
    return count



def parse_tags(tweet):
    """
    (provided)
    Given a tweet like '@bob: this #is #it', returns
    a list of tags like ['#is', '#it'].
    >>> parse_tags('This #tweet is #fire')
    ['#tweet', '#fire']
    >>> parse_tags('@user: #tag1 #tag2')
    ['#tag1', '#tag2']
    >>> parse_tags('This tweet is on fire')
    []
    >>> parse_tags('A # starts a Python comment')
    []
    >>> parse_tags('#run#together')
    ['#run', '#together']
    """
    hash_tags = []
    search = 0
    while True:
        hash = tweet.find('#', search)
        if hash == -1:
            break

        end = hash + 1
        # isalnum() = alpha or digit
        while end < len(tweet) and tweet[end].isalnum():
            end += 1

        hash_tag = tweet[hash:end]
        if len(hash_tag) > 1:
            hash_tags.append(hash_tag)
        search = end  # tricky: #tags#adjacent
    return hash_tags

if __name__ == "__main__":
    main()