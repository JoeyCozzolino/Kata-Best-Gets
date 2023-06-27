'''
Introduction
The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

Task
Given a year, return the century it is in.
'''

import math
def century(year):
    yearcheck = year % 100
    if yearcheck == 0:
        return year / 100
    if yearcheck != 0:
        return math.floor(year / 100 + 1)

# https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097