def print_course_info(explore_courses, course_id, info):
    """
    Given a nested dictionary of courses and their information, a specific course id, and a specific type
    of information to print about that course id. The function should print out the information if the
    dictionary has that information for the given course. If the course is in the dictionary, but it does
    not have that information stored, it should print 'We do not have that information for the given course.'
    If the course is not in the dictionary at all, it should print 'Sorry, that course is not in our system.'
    """
    pass

def add_price(name, gas_type, price, gas_prices):
    """
    Given the name of a gas station (e.g. "Speedway"), the type of gas (e.g. "unleaded"), and a price (e.g. 3.50)
    and adds it to the also passed in gas_prices dictionary (which is ultimately returned). The gas prices dictionary
    should be set up so that each key is a different gas station and each value is another dictionary where the key
    is the type of gas and the value is the gas price. If there is already a price for a given gas station / gas type
    pairing, overwrite it.

    >>> >>> add_price('Speedway', 'unleaded', 3.50, {})
    {'Speedway' : {'unleaded' : 3.50}}
    """
    pass

def first_list(strs):
    """
    Given a list of strings, create and return a dictionary whose keys are the
    unique first characters of the strings and whose values are lists of words
    beginning with those characters, in the same order that they appear in strs.
    >>> first_list(['To', 'be', 'or', 'not', 'to', 'be:', 'that', 'is', 'the', 'question'])
    {'T': ['To'], 'b': ['be', 'be:'], 'o': ['or'], 'n': ['not'], 't': ['to', 'that', 'the'], 'i': ['is'], 'q': ['question']}
    >>> first_list(['I', 'say', 'I', 'wonder', "what's", 'going', 'to', 'happen', 'exciting', 'today?'])
    {'I': ['I', 'I'], 's': ['say'], 'w': ['wonder', "what's"], 'g': ['going'], 't': ['to', 'today?'], 'h': ['happen'], 'e': ['exciting']}
    """
    pass

def suffix_list(strs):
    """
    Given a list of strings, create and return a dictionary whose keys are the suffixes
    of those strings and whose values are lists of words ending with those suffixes, in
    the same order that they appear in strs. A suffix is defined as the last 2 characters of a string,
    and a string that is less than 2 characters long has no suffix.
    >>> suffix_list(['investigator', 'reporter', 'professor', 'wild', 'bit', 'child', 'doctor', 'spacesuit'])
    {'or': ['investigator', 'professor', 'doctor'], 'er': ['reporter'], 'ld': ['wild', 'child'], 'it': ['bit', 'spacesuit']}
    """
    pass