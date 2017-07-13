def twoSum(self, nums, target):
    d = {}
    for i, num in enumerate(nums):
        if d.get(target-num) != None:
            return [d[target-num],i]
        else:
            d[num] = i
            