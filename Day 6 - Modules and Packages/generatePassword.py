import random, string


UPPER = string.ascii_uppercase
LOWER = string.ascii_lowercase
DIGITS = string.digits
SPECIAL_CHAR = string.punctuation
All_CHAR = UPPER + LOWER + DIGITS + SPECIAL_CHAR


def gP():
    Passw = random.choice(UPPER) + random.choice(LOWER) + random.choice(DIGITS) + random.choice(SPECIAL_CHAR)
    password = Passw + "".join(random.choices(All_CHAR, k=4))
    print(password)
    return

gP()    