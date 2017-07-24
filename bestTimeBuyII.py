def maxProfit(prices):
    maxProfit, minPrice = 0, float("inf")
    for price in prices:
        minPrice = min(minPrice,price)
        profit = price - minPrice
        maxProfit = (maxProfit,profit)
    return maxProfit