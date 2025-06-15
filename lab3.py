# LAB 3 - RECURSIVE FUNCTIONS




# RECURSIVE FACTORIAL FUNCTION
def factorial(number):
    # BASE CASE: 0! = 1
    if number == 0:
        return 1
    else:
        # RECURSIVE CASE: n! = n * (n-1)!
        return number * factorial(number - 1)




# HELPER FUNCTION FOR LINEAR SEARCH
def linear_search_helper(lst, key, index):
    # BASE CASE: IF INDEX EXCEEDS LENGTH, KEY NOT FOUND
    if index >= len(lst):
        return -1
    # IF CURRENT ELEMENT MATCHES KEY, RETURN INDEX
    if lst[index] == key:
        return index
    # RECURSIVE CALL ON NEXT INDEX
    return linear_search_helper(lst, key, index + 1)





# RECURSIVE LINEAR SEARCH FUNCTION
def linear_search(lst, key):
    # START SEARCH AT INDEX 0
    return linear_search_helper(lst, key, 0)




# HELPER FUNCTION FOR BINARY SEARCH
def binary_search_helper(lst, key, low, high):
    # BASE CASE: IF SEARCH SPACE IS EMPTY, RETURN -1
    if low > high:
        return -1
    # FIND MIDPOINT
    mid = (low + high) // 2
    # CHECK IF MIDDLE ELEMENT IS THE KEY
    if lst[mid] == key:
        return mid
    # IF KEY IS SMALLER, SEARCH LEFT HALF
    elif key < lst[mid]:
        return binary_search_helper(lst, key, low, mid - 1)
    # IF KEY IS LARGER, SEARCH RIGHT HALF
    else:
        return binary_search_helper(lst, key, mid + 1, high)




# RECURSIVE BINARY SEARCH FUNCTION
def binary_search(lst, key):
    # START SEARCH WITH FULL LIST RANGE
    return binary_search_helper(lst, key, 0, len(lst) - 1)