def singleNum1(self,nums):
    res = 0
    for num in nums:
        res ^= num
    return res


import operator
from functools import reduce

def singleNum2(self,nums):
    return reduce(operator.xor, nums)

def singleNum3(self,nums):
    return reduce(lambda x, y:x^y, nums)


def singleNum4(self,nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num,0)+1
    for key,val in dic:
        if val == 1:
            return key