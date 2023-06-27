'''
Check to see if a string has the same amount of 'x's and 'o's. 
The method must return a boolean and be case insensitive. The string can contain any char.
'''


def xo(s):
    list_1 = []
    list_2 = []
    for letters in s:
        if letters == "x" or letters == "X":
            list_1 += "x"
        if letters == "o" or letters == "O":
            list_2 += "o"
    if len(list_1) == len(list_2):
        return True
    else:
        return False