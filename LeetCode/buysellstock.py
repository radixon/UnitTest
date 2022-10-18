def maxProfit(prices):
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a 
    different day in the future to sell that stock.
    
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    """
    ans = 0
    subarray = float('inf')
    for value in prices:
        subarray = min(value,subarray)
        ans = max(value-subarray,ans)
    
    return ans