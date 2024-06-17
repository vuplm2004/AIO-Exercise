def my_function(my_list):
    max_list = my_list[0]
    for i in my_list:
        if i > max_list:
            max_list = i
        else:
            continue
    return max_list


if __name__ == "__main__":
    my_list = [1001, 9, 100, 0]
    assert my_function(my_list) == 1001

    my_list = [1, 9, 9, 0]
    print(my_function(my_list))
