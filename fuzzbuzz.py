class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rtnList = []
        for i in range(1,n+1):
            if i%15 == 0 and i >= 15:
                rtnList.append("FizzBuzz")
            elif i%3 == 0 and i >= 3:
                rtnList.append("Fizz")
            elif i%5 == 0 and i >= 5:
                rtnList.append("Buzz")
            else:
                rtnList.append(str(i))
        return rtnList