"""

iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd

"""

"""
# my solution

def iq_test(numbers):
    nums = list(map(int, numbers.split(' ')))
    priznak = nums[0]%2
    k = 1
    for n in nums[1:-1]:
        if n%2 != priznak:
            if nums[k+1]%2 != priznak:
                return k
            else:
                return k+1
        k+=1
    return len(nums)
    
"""

def iq_test(n):
    n = [int(i)%2 for i in n.split()]
    if n.count(0)>1:
        return n.index(1)+1
    else:
        return n.index(0)+1