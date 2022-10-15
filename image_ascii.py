import math
import cv2

CHARS = [".", ",", ":", ";", "+", "*", "?", "%", "S", "#", "@"]
INVERTED_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# def image_to_ascii():
#     # Get the source
#     source = cv2.Mat(100, 100, cv2.CV_8UC4)
#     frame = source

#     # Make it gray
#     newMat = cv2.Mat()
#     cv2.cvtColor(frame, newMat, cv2.COLOR_RGBA2GRAY)

#     # Make it ascii
#     data = frame.data
#     characters = ""
#     characterLine = ""
#     for rows in range(frame.rows):
#         for cols in range(frame.cols - 1, -1, -1):
#             pixel = data[rows * frame.cols + cols]
#             newChar = CHARS[math.floor(pixel / 25)]
#             characterLine += newChar
    
#         characterLine += "\n"
#         characters += characterLine
#         characterLine = ""
    
#     return characters


def video_frames(path):
    vidObj = cv2.VideoCapture(path)
    count = 0

    success = 1
  
    while success:
        success, image = vidObj.read()

        if image is None:
            break

        image = cv2.resize(image, (100, 100));
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2GRAY)

        # do stuff with "image"
        #cv2.imwrite("output/frame%d.png" % count, image)
  
        count += 1
        #return



if __name__ == "__main__":
    video_frames("vid.mp4")


