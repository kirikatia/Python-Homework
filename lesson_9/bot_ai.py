import random

def make_move(candies):
    losing_state = int(candies / 29) * 29
    k = candies - losing_state
    k = random.randint(1, 28) if k <= 0 else k
    return k