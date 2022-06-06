import random


adjectives = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']
my_tuple = (1, 2, 3)


def random_phrase():
    rand_adj = random.choice(adjectives)
    rand_noun = random.choice(nouns)
    return rand_adj + " " + rand_noun

def random_float(min_val, max_val):
    return random.uniform(min_val, max_val)

def random_bowling_score():
    return random.randint(0, 300)

def silly_tuple():
    return (random_phrase(), random_float(1.0, 5.0), random_bowling_score())
