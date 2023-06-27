'''
Write a function that takes an array of strings as an argument and returns a sorted array containing the same strings, ordered from shortest to longest.
'''

def sort_by_length(arr):
    sorted_list = sorted(arr, key=len)
    return sorted_list