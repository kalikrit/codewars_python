"""
на входе строка s 0 < len(s) < 100
нужно вернуть середину строки
  'test' => 'es'
  'a' => 'a'
  'bac' => 'a'
"""
"""
мое решение

def get_middle(s):
    midx = len(s)//2
    if len(s)%2 == 0:
        return s[midx-1:midx+1]
    else:
        return s[midx:midx+1]
"""

def get_middle(string):
    """
    best practices
    """
    return string[(len(string)-1)/2 : len(string)/2+1]
