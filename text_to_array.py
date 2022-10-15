import numpy as np

BRIGHTNESS_CHARS = [".", ",", ":", ";", "+", "*", "?", "%", "S", "#", "@"]
BRIGHTNESS_INVERTED_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def text_file_to_array(filename):
    array = np.ndarray((100, 100, 3))
    with open(filename) as in_file:
        line_num = 0
        for line in in_file.readlines():
            line = line.strip()
            char_num = 0
            for character in line:
                character_value = BRIGHTNESS_CHARS.index(character) / len(BRIGHTNESS_CHARS)
                array[line_num][char_num] = [character_value, character_value, character_value]
                char_num += 1
            line_num += 1
    return array


if __name__ == "__main__":
    array = text_file_to_array("art.txt")
    print(array)
