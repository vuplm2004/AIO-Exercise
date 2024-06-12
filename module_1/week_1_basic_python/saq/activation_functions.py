import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def relu(x):
    return max(0, x)


def elu(x, alpha=0.1):
    return x if x > 0 else alpha * (math.exp(x) - 1)


def is_number(x):
    try:
        float(x)

    except ValueError:
        return False
    return True


def exercise2():
    while True:
        x = input("Input x = ")
        if is_number(x):
            x = float(x)
            break
        else:
            print("x must be a number")
            return False

    activation_function = input("Input activation Function (sigmoid|relu|elu): ")

    if activation_function.lower() == "sigmoid":
        result = sigmoid(x)
        print(f"sigmoid: f({x}) {result:.4f}")
    elif activation_function.lower() == "relu":
        result = relu(x)
        print(f"relu: f({x}) {result:.4f}")
    elif activation_function.lower() == "elu":
        result = elu(x)
        print(f"elu: f({x}) {result:.4f}")
    else:
        print(f"{activation_function} is not supported")

if __name__ == "__main__":
    exercise2()