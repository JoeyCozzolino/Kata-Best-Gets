'''
Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.
'''


def shortcut( s ):
    # ...
    final = ""
    vowels = ["a", "e", "i", "o", "u"]
    for letters in s:
        if letters in vowels:
            continue
        else:
            final += letters
    return final


# https://www.codewars.com/kata/5547929140907378f9000039