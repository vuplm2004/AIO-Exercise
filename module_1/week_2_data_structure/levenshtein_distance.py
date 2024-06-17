def levenshtein_distance(source, target):
    # create matrix
    height = len(source)
    width = len(target)
    d = [[0 for _ in range(width + 1)] for _ in range(height + 1)]
    # now we have an empty matrix D

    # fill first column with number of deletion needed
    for i in range(height + 1):
        d[i][0] = i
    # fill first row with number of insertion needed
    for j in range(width + 1):
        d[0][j] = j

    for i in range(1, height + 1):
        for j in range(1, width + 1):
            if source[i - 1] == target[j - 1]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] +
                          1, d[i - 1][j - 1] + cost)

    return d[height][width]


if __name__ == "__main__":
    assert levenshtein_distance("hi", "hello") == 4
    print(levenshtein_distance("hola", "hello"))
