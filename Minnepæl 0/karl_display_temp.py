#!/bin/python3
from sense_hat import SenseHat
import time

sense = SenseHat()

r = (255, 0, 0)
b = (0, 0, 255)
w = (255, 255, 255)
sense.set_rotation(270)

n_0 = [[0, 0], [1, 0], [2, 0], [0, 1], [2, 1], [0, 2], [2, 2], [0, 3], [2, 3], [0, 4], [1, 4], [2, 4]]
n_1 = [[2, 0], [2, 1], [2, 2], [2, 3], [2, 4]]
n_2 = [[0, 0], [1, 0], [2, 0], [2, 1], [0, 2], [1, 2], [2, 2], [0, 3], [0, 4], [1, 4], [2, 4]]
n_3 = [[0, 0], [1, 0], [2, 0], [2, 1], [0, 2], [1, 2], [2, 2], [2, 3], [0, 4], [1, 4], [2, 4]]
n_4 = [[0, 0], [2, 0], [0, 1], [2, 1], [0, 2], [1, 2], [2, 2], [2, 3], [2, 4]]
n_5 = [[0, 0], [1, 0], [2, 0], [0, 1], [0, 2], [1, 2], [2, 2], [2, 3], [0, 4], [1, 4], [2, 4]]
n_6 = [[0, 0], [1, 0], [2, 0], [0, 1], [0, 2], [1, 2], [2, 2],[0, 3], [2, 3], [0, 4], [1, 4], [2, 4]]
n_7 = [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4]]
n_8 = [[0, 0], [1, 0], [2, 0], [0, 1], [2, 1], [0, 2], [1, 2], [2, 2], [0, 3], [2, 3], [0, 4], [1, 4], [2, 4]]
n_9 = [[0, 0], [1, 0], [2, 0], [0, 1], [2, 1], [0, 2], [1, 2], [2, 2], [2, 3], [0, 4], [1, 4], [2, 4]]
neg = [[0, 1], [1, 1], [2, 1]]
pos = [[1, 0], [0, 1], [1, 1], [2, 1], [1, 2]]
err = [[0, 0], [1, 0], [2, 0], [0, 1], [0, 2], [1, 2], [2, 2], [0, 3], [0, 4], [1, 4], [2, 4]]
nums = [n_0, n_1, n_2, n_3, n_4, n_5, n_6, n_7, n_8, n_9, neg, pos, err]


def printNm(nm, nm_lst):
  sense.clear()
  if nm < 0:
    for pix in nm_lst[10]:
      sense.set_pixel(pix[0], pix[1], b)
  elif nm > 0:
    for pix in nm_lst[11]:
      sense.set_pixel(pix[0], pix[1], r)
  if nm > 99 or nm < -99:
    for pix in nm_lst[12]:
      sense.set_pixel(1+pix[0], 3+pix[1], w)
    for pix in nm_lst[12]:
      sense.set_pixel(5+pix[0], 3+pix[1], w)
  elif (-10 < nm < 0) or (0 < nm < 10):
    for pix in nm_lst[int(str(abs(nm))[0])]:
      sense.set_pixel(5+pix[0], 3+pix[1], w)
  elif nm == 0:
    for pix in nm_lst[0]:
      sense.set_pixel(5+pix[0], 3+pix[1], w)
  else:
    for pix in nm_lst[int(str(abs(nm))[0])]:
      sense.set_pixel(1+pix[0], 3+pix[1], w)
    for pix in nm_lst[int(str(abs(nm))[1])]:
      sense.set_pixel(5+pix[0], 3+pix[1], w)

while True:
  temp = int(sense.get_temperature())
  printNm(temp, nums)
  time.sleep(0.1)
  