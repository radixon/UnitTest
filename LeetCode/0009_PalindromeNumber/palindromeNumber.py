def isPalindrome(x):
    """
    Given an integer x, return true if x is a 
    palindrome, and false otherwise.
    """
    if x < 0: return False
    if x > 0 and x%10 == 0: return False
    z, y = x, 0
    while z > 0:
        y = y*10 + z%10
        z //= 10
    return x == y