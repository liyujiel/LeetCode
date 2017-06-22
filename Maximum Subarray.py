def MaxSubarray(self,nums):
    # Set maxSum as return value, currSum compared with next num
    maxSum = currSum = nums[0]
    for num in nums[1:]:
        currSum = max(num,currSum+num)
        maxSum = max(currSum,maxSum)
    return maxSum

def maxSubarray(self,nums):
    for i in xrange(1,len(nums)):nums[i]=max(nums[i],nums[i]+nums[i-1])
    return max(nums)