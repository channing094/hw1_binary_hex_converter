# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cxAYmY7mf22fo4I7uXzvB3nlveS7e__u
"""

number = input()
number = int(number)

if number >= 128 :
  number = number - 128
  n1 = 1
else:
  n1 = 0

if number >= 64 :
  number = number - 64
  n2 = 1
else:
  n2 = 0

if number >= 32 :
  number = number - 32
  n3 = 1
else:
  n3 = 0

if number >= 16 :
  number = number - 16
  n4 = 1
else:
  n4 = 0

if number >= 8 :
  number = number - 8
  n5 = 1
else:
  n5 = 0

if number >= 4 :
  number = number - 4
  n6 = 1
else:
  n6 = 0

if number >= 2 :
  number = number - 2
  n7 = 1
else:
  n7 = 0

if number >= 1 :
  number = number - 1
  n8 = 1
else:
  n8 = 0

answer = str(n1) + str(n2) + str(n3) + str(n4) + str(n5) + str(n6) + str(n7) + str(n8)

print(answer)