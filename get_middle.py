"""
на входе строка s 0 < len(s) < 100
надо вернуть середину строки:
  'es' для 'test'
  'a' для 'a'
  'a' для 'bac'
"""

'''
# мое решение

def get_middle(s):
    midx = len(s)//2
    if len(s)%2 == 0:
        return s[midx-1:midx+1]
    else:
        return s[midx:midx+1]
'''        
    
# best practices

def get_middle(s):
   return s[(len(s)-1)/2:len(s)/2+1]