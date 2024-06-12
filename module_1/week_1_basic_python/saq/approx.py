import math


def factorial(x):
    product = 1
    for i in range(x):
        product *= i + 1
    return product


def approx_sin(x, n):
    sin = 0
    for i in range(n):
        sin += ((-1) ** i) * ((x ** (2 * i + 1)) / factorial(2 * i + 1))
    return sin


def approx_cos(x, n):
    cos = 0
    for i in range(n):
        cos += ((-1) ** i) * ((x ** (2 * i)) / factorial(2 * i))
    return cos


def approx_sinh(x, n):
    sinh = 0
    for i in range(n):
        sinh += (x ** (2 * i + 1)) / factorial(2 * i + 1)
    return sinh


def approx_cosh(x, n):
    cosh = 0
    for i in range(n):
        cosh += (x ** (2 * i)) / factorial(2 * i)
    return cosh


def exercise4():
    x = float(input("Input x (gradient): "))
    n = int(input("Input number of loops: "))
    if not isinstance(x, float):
        print("x must be float")
    elif not isinstance(n, int):
        print("n must be int")
    else:
        if n > 0:
            print(f"approx_sin(x={x}, n={n}) =", approx_sin(x, n))
            print(f"approx_cos(x={x}, n={n}) =", approx_cos(x, n))
            print(f"approx_sinh(x={x}, n={n}) =", approx_sinh(x, n))
            print(f"approx_cosh(x={x}, n={n}) =", approx_cosh(x, n))
        else:
            print("n must be greater than zero")


if __name__ == "__main__":
    exercise4()
