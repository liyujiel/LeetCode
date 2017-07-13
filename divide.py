def divide(self, dividend, divisor):
    sign = (dividend > 0 ) is (divisor >0 )
    dividend, divisor = abs(dividend), abs(divisor)
    res = 0
    while dividend > divisor:
        temp, val = divisor, 1
        while dividend > temp:
            res += val
            dividend -= temp
            temp += temp
            val += val
    
    if not sign:
        res = -res
    
    return min(max(-2147483648,res),2147483648)