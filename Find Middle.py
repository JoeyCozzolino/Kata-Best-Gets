'''
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.
'''


def get_middle(s):
    while len(s) > 2:
        s = s [1:-1]
    return s

# https://www.codewars.com/kata/56747fd5cb988479af000028