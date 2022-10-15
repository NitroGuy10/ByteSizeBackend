import cv2
import time
import numpy as np
import math

height = 480
width = 640
chars = [".", ",", ":", ";", "+", "*", "?", "%", "S", "#", "@"]
#chars = [' ', '`','^','"',',',':',';','I','l','!','i','~','+','_','-','?',']',
#        '[','}','{','1',')','(','|','/','t','f','j','r','x','n','u','v','c','z',
 #       'X','Y','U','J','C','L','Q','0','O','Z','m','w','q','p','d','b','k','h',
 #       'a','o','*','#','M','W','&','8','%','B','@','$']
def resizeImg(img, newWidth):
    newMat = cv2.Mat(np.zeros((1,1)))
    width = len(img[0]);
    height = len(img);
    ratio = height / width;
    newHeight = math.floor(newWidth * ratio * 0.75)

    newMat = cv2.resize(img, (newWidth, newHeight))
    return newMat;

def grayify(img):
  return cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)

def asciify(img):
  data = img;
  characters = "";
  characterLine = "";
  for rows in range(len(img)):
    for cols in range(len(img[0])):
      #pixel = data[rows * len(img[0]) + cols]
      pixel = data[rows][cols]
      #newChar = chars[math.floor(pixel / 4)]
      newChar = chars[math.floor(pixel / 25)]
      characterLine += newChar

    characterLine += "\n"
    characters += characterLine
    characterLine = ""

  print(characters)
  return characters


def printMat(img):
  print(type(img))
  for row in img:
    for elem in row:
      print(elem)

def processVideo(filename):
  #src = cv2.Mat(480, 640, cv2.CV_8UC4)
  src = cv2.Mat(np.zeros((480, 640, 4), dtype='uint8'))
  cap = cv2.VideoCapture(filename)
  _, src = cap.read(src)
  while(src is not None):
    #src = cv2.imread('goldengate.jpg')
    frame = resizeImg(src, 120);
    frame = grayify(frame);
    characters = asciify(frame);
    #TODO: Put characters into a text file and do whatever with it
    _, src = cap.read(src)


processVideo("testvid.mp4")

