"""
accum("abcd")    # "A-Bb-Ccc-Dddd"
accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt")    # "C-Ww-Aaa-Tttt"
"""

"""
# мое решение

def accum(s):
    result = ''
    k = 1
    for l in s:
        result += (l*k).title()
        if k < len(s):
            result += '-'
        k+=1
    return result
    
"""

# Best practices

def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))