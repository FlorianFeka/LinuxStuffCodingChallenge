# This problem was asked by Facebook.

# Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

from lazy_streams import stream
import random

data = stream(range(100))

def getItem(data):
    return data.filter(lambda i: bool(random.getrandbits(1))).first_or_else()

print(getItem(data))

