import math
import random


def mae(n, y, yhat):
    loss = 0
    for i in range(n):
        loss += (abs(y[i] - yhat[i])) / n
        print(
            f"loss name: MAE, sample: {i+1}, predict: {yhat[i]}, target: {y[i]}, loss = {loss}"
        )
    print(f"final MAE = {loss}")


def mse(n, y, yhat):
    loss = 0
    for i in range(n):
        loss += ((y[i] - yhat[i]) ** 2) / n
        print(
            f"loss name: MSE, sample: {i+1}, predict: {yhat[i]}, target: {y[i]}, loss = {loss}"
        )
    print(f"final MSE = {loss}")


def rmse(n, y, yhat):
    loss = 0
    for i in range(n):
        loss += math.sqrt(((y[i] - yhat[i]) ** 2) / n)
        print(
            f"loss name: RMSE, sample: {i+1}, predict: {yhat[i]}, target: {y[i]}, loss = {loss}"
        )
    print(f"final RMSE = {loss}")


def exercise3():
    while True:
        n = input("Input umber of samples (integer) which are generated: ")
        if n.isnumeric():
            n = int(n)

            y = [random.uniform(0, 10) for i in range(n)]
            yhat = [random.uniform(0, 10) for i in range(n)]

            loss_func = input("Input loss name ( MAE | MSE | RMSE ): ")
            if loss_func.lower() == "mae":
                mae(n, y, yhat)
                break
            elif loss_func.lower() == "mse":
                mse(n, y, yhat)
                break
            elif loss_func.lower() == "rmse":
                rmse(n, y, yhat)
                break
            else:
                print(f"{loss_func} is not supported")
        else:
            print("Number of samples must be integer")


if __name__ == "__main__":
    exercise3()
