import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


# Test cases
assert round(sigmoid(3), 2) == 0.95
print(round(sigmoid(2), 2))
