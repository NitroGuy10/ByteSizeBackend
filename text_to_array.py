import numpy as np
import re

BRIGHTNESS_CHARS = [".", ",", ":", ";", "+", "*", "?", "%", "S", "#", "@"]
BRIGHTNESS_INVERTED_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
BRIGHTNESS_EXTENDED_CHARS = [' ', '`','^','"',',',':',';','I','l','!','i','~','+','_','-','?',']',
        '[','}','{','1',')','(','|','/','t','f','j','r','x','n','u','v','c','z',
       'X','Y','U','J','C','L','Q','0','O','Z','m','w','q','p','d','b','k','h',
       'a','o','*','#','M','W','&','8','%','B','@','$']
CHOSEN_BRIGHTNESS_CHARS = BRIGHTNESS_EXTENDED_CHARS


def ascii_video_string_to_array(video_string: str):
    height = 60
    width = 120
    video_string = video_string.strip()
    lines = video_string.split("\n")
    num_frames = ((len(lines) - 1) // height) + 1

    array = np.ndarray((num_frames, height, width))
    for overall_line_num in range(len(lines)): 
        line_num = overall_line_num % height    
        frame_num = overall_line_num // height
        line = lines[overall_line_num]
        for char_num in range(len(line)):
            character = line[char_num]
            character_value = CHOSEN_BRIGHTNESS_CHARS.index(character) / (len(CHOSEN_BRIGHTNESS_CHARS) - 1)
            array[frame_num][line_num][char_num] = character_value
    return array

# def text_file_to_array(filename):
#     array = np.ndarray((60, 120, 3))
#     with open(filename) as in_file:
#         line_num = 0
#         for line in in_file.readlines():
#             line = line.strip()
#             char_num = 0
#             for character in line:
#                 character_value = BRIGHTNESS_CHARS.index(character) / (len(BRIGHTNESS_CHARS) - 1)
#                 array[line_num][char_num] = [character_value, character_value, character_value]
#                 char_num += 1
#             line_num += 1
#     return array


if __name__ == "__main__":
    with open("res.txt") as in_file:
        file_text = in_file.read()
        array = ascii_video_string_to_array(file_text)

        print(array[0])
        print(array[315])
