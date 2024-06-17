def my_function(my_list):
    min_list = my_list[0]
    for i in my_list:
        if i < min_list:
            min_list = i
        else:
            continue
    return min_list


if __name__ == "__main__":
    my_list = [1, 22, 93, -100]
    assert my_function(my_list) == -100

    my_list = [1, 2, 3, -1]
    print(my_function(my_list))
