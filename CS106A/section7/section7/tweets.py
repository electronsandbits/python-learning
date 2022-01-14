#!/usr/bin/env python3
import sys


def reverse_alpha_keys(flat_counts):
    """
    Given a flat_counts dictionary, prints out the hashtags in reverse aplphabetical order.
    """
    pass


def most_used(flat_counts):
    """
    Takes in a 'flat' dictionary as described above, and prints the 10 most frequently
    used hashtags in the dataset.
    """
    pass

#Below are all of the functions from last week's section

def flat_counts(user_tags):
    """
    (Extension Problem)
    Given a user_tags dicts, sum up the tag counts across all users,
    return a "flat" counts dict with a key for each tag,
    and its value is the sum of that tag's count across users.
    >>> flat_counts({'@alice': {'#apple': 1, '#banana': 2}, '@bob': {'#apple': 1}})
    {'#apple': 2, '#banana': 2}
    """
    counts = {}
    for user in user_tags.keys():
        tags = user_tags[user]
        for tag in tags:
            if tag not in counts:
                counts[tag] = 0
            counts[tag] += tags[tag]
    return counts

def add_tweet(user_tags, tweet):
    """
    Given a user_tags dict and a tweet, parse out the user and tags,
    and add those counts to the user_tags dict which is returned.
    If no user exists in the tweet, return the user_tags dict unchanged.
    Note: call the parse_tags(tweet) and parse_user(tweet) functions to pull
    the parts out of the tweet.
    >>> add_tweet({}, '@alice: #apple banana')
    {'@alice': {'#apple': 1}}
    >>> add_tweet({'@alice': {'#apple': 1, '#banana': 1}}, '@alice: #banana')
    {'@alice': {'#apple': 1, '#banana': 2}}
    >>> add_tweet({'@alice': {'#apple': 1, '#banana': 2}}, '@bob: #apple')
    {'@alice': {'#apple': 1, '#banana': 2}, '@bob': {'#apple': 1}}
    """
    user = parse_user(tweet)
    if user == '':
        return user_tags

    # if user is not in there, put them in with empty counts
    if user not in user_tags:
        user_tags[user] = {}

    # counts is the nested tag -> count dict
    # go through all the tags and modify it
    counts = user_tags[user]
    tag = parse_tag(tweet)
    if tag != '':
        if tag not in counts:
            counts[tag] = 0
        counts[tag] += 1
    return user_tags


def parse_tweets(filename):
    """
    Given a file of tweets, 1 per line, build and return a user_tags dict
    of all the tweet data.
    """
    user_tags = {}
    # here we specify encoding 'utf-8' which is how this text file is encoded
    # python technically does this by default, but it's better to be explicit
    with open(filename, encoding='utf-8') as f:
        for line in f:
            add_tweet(user_tags, line)
    return user_tags



"""
Feel free to peruse the code below here,
but it isn't necessary to solve the problem.
"""
def parse_tag(tweet):
    hash = tweet.find('#')
    if hash == -1:
        return ''

    end = hash + 1
    # isalnum() = alpha or digit
    while end < len(tweet) and tweet[end].isalnum():
        end += 1

    hash_tag = tweet[hash:end]
    return hash_tag


def parse_user(tweet):
    """
    (provided)
    Given a tweet like '@bob: hello #woot', returns
    the user '@bob' or '' if no user is found.
    >>> parse_user('@jonathan: tweet')
    '@jonathan'
    >>> parse_user('@ThisIsATest: #oh #yeah')
    '@ThisIsATest'
    >>> parse_user('meh')
    ''
    """
    colon = tweet.find(':')
    if colon == -1:
        return ''
    return tweet[:colon]


def print_counts(tags):
    """
    (provided)
    Given a counts dict mapping tag -> count, prints
    out the tags in order like
      #apple -> 13
      #boat -> 1
      #zebra -> 12
    """
    for tag in sorted(tags.keys()):
        print(' ' + tag + ' -> ' + str(tags[tag]))
        # alternate technique: str.format() like this:
        # print(' {} -> {}'.format(tag, tags[tag]))

def main():
    args = sys.argv[1:]
    # 5 ways to run from terminal:
    # filename            # prints out all users and tag_counts
    # -users filename     # prints just user names
    # -user user filename # prints data for a particular user
    # -flat filename      # prints flat tag counts
    # -most filename      # prints most common tag

    # args: filename
    if len(args) == 1:
        user_tags = parse_tweets(args[0])
        for user in sorted(user_tags.keys()):
            print(user)
            counts = user_tags[user]
            print_counts(counts)

    # args: -users filename
    if len(args) == 2 and args[0] == '-users':
        # args[1] is tweets
        user_tags = parse_tweets(args[1])
        print('users')
        for user in sorted(user_tags.keys()):
            print(user)

    # args: -user user filename
    if len(args) == 3 and args[0] == '-user':
        # args[1] is user, args[2] is tweets
        user_tags = parse_tweets(args[2])
        print('user:', args[1])
        counts = user_tags[args[1]]  # pull out tags for just that user
        print_counts(counts)

    # args: -flat filename
    if len(args) == 2 and args[0] == '-flat':
        user_tags = parse_tweets(args[1])
        counts = flat_counts(user_tags)
        print('flat')
        print_counts(counts)

    # args: -most filename
    if len(args) == 2 and args[0] == '-most':
        user_tags = parse_tweets(args[1])
        counts = flat_counts(user_tags)
        print('most')
        most_used(counts)


if __name__ == '__main__':
    main()
