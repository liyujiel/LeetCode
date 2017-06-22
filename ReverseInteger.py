def reverse(self,s):
    maxBit, minBit = (2**32 - 1)/2, -(2*32 - 1)/2
    if s < 0:
        res = -int(str(s[1:][::-1]))
    else:
        res = int(str(s[::-1]))
    if res > maxBit or res < minBit:
        res = 0
    return res