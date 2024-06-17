def my_function(integers, number):
    tf_list = []
    for i in integers:
        if i == number:
            tf_list.append(True)
        else:
            tf_list.append(False)

    return any(tf_list)


if __name__ == "__main__":
    my_list = [1, 3, 9, 4]
    assert my_function(integers=my_list, number=-1) == False

    my_list = [1, 2, 3, 4]
    print(my_function(integers=my_list, number=2))
