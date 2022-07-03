# Solution - 1 : Brute Force 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if(prices[i]<prices[j]):
                    maxp=max(maxp,prices[j]-prices[i])
        return maxp


# Solution -2 : Using Two Pointers

def maximumProfit(prices):
    # Write your code here
    l,r=0,1
    maxp=0
    while r<len(prices):
        if(prices[l]<prices[r]):
            maxp=max(maxp,prices[r]-prices[l])
        else:
            l=r
        r+=1
    return maxp


# Solution 3 - Using Optimised Method

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        minp=100000000000
        for i in range(len(prices)):
            minp=min(minp,prices[i])
            maxp=max(maxp,prices[i]-minp)
        return maxp