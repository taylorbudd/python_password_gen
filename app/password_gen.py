import random


# returning a random alpha character that is capitalized (A-Z)
def random_capitalized_alpha_char():
    return chr(random.randint(65, 90))


# returning random lowercase alpha character (a-z)
def random_lower_alpha_char():
    return chr(random.randint(97, 122))


# returning a random special character
def random_special_char():

    special_char_ascii_nums = [33, 35, 36, 37, 38, 40, 41, 63, 64, 124]
    random_index = random.randint(0, len(special_char_ascii_nums))



