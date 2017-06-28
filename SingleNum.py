def singleNum1(self,nums):
    res = 0
    for num in nums:
        res ^= num
    return res


import operator
from functools import reduce

def singleNum2(self,nums):
    return reduce(operator.xor, nums)