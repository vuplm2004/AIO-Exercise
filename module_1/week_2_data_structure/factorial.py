def my_function(y):
    var = 1
    for i in range(1, y+1):
        var *= i

    return var


if __name__ == "__main__":
    assert my_function(8) == 40320
    print(my_function(4))
