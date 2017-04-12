"""
Task
    Given a string str, find the shortest possible string which can be achieved
    by adding characters to the end of initial string to make it a palindrome.

Example
    For str = "abcdc", the output should be "abcdcba".

Input/Output
    [input] string str
    A string consisting of lowercase latin letters.

Constraints: 3 ≤ str.length ≤ 10.
[output] a string
"""
"""
# my solution

def is_palindrome(string):
    '''
    checks whether the given string is a palindrome
    '''
    return string == string[::-1]


def build_palindrome(string):
    '''
    makes palindrom out of the given string
    '''
    if is_palindrome(string):
        return string
    else:
        i = 0
        for _ in string:
            new_str = string + string[i::-1]
            if is_palindrome(new_str):
                return new_str
            i += 1
"""


def build_palindrome(some_str):
    """
    best practices
    """
    suf = ""
    for let in some_str:
        pal = some_str + suf
        if pal == pal[::-1]:
            return pal
        suf = let + suf


# print(build_palindrome('abcd'))
