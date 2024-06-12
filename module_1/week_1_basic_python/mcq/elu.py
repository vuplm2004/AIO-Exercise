import math


def elu(x, alpha=0.01):
    if x <= 0:
        return alpha * (math.exp(x) - 1)
    else:
        return x


# Test cases
assert round(elu(1)) == 1
print(round(elu(-1), 2))
