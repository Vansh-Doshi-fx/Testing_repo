from patterns_print import *

print("hello World!")
printFirstTenNum()
print()
printStars(5)

def is_palindrome(s):
    """Checks if the given string is a palindrome.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    return s == s[::-1]