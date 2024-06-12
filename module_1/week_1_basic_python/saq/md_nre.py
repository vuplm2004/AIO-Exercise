import math


def md_nre_single_sample(y, yhat, n, p):
    result = (y ** (1 / n) - yhat ** (1 / n)) ** p
    return print(result)


md_nre_single_sample(y=100, yhat=99.5, n=2, p=1)
md_nre_single_sample(y=50, yhat=49.5, n=2, p=1)
md_nre_single_sample(y=20, yhat=19.5, n=2, p=1)
md_nre_single_sample(y=0.6, yhat=0.1, n=2, p=1)
