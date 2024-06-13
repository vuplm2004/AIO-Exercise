
def word_count(file_path):
    with open(file_path, "r") as file:
        file_data = file.read()
        file_words = file_data.split()

        counter = {}
        for word in file_words:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
    return counter


if __name__ == "__main__":
    file_path = "C:/Users/Admin/Desktop/AIO2024/AIO-Exercise/module_1/week_2_data_structure/P1_data.txt"
    result = word_count(file_path)
    assert result['who'] == 3
    print(result['man'])
