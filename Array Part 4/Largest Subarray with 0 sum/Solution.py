# BRUTE FORCE SOLUTION APPROACH

def LongestSubsetWithZeroSum(arr):
    
    # Initialize result
    maxLen = 0
    n = len(arr)

    # Pick a starting point
    for i in range(n):

        # Initialize currSum for every starting point
        currSum = 0

        # Try all subarrays starting with 'i'
        for j in range(i, n):
            currSum += arr[j]

            # If currSum becomes 0,then update maxLen if required

            if currSum == 0:
                maxLen = max(maxLen, j - i + 1)

    
    return maxLen


# OPTIMISED APPROACH

'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    Where 'N' denotes the number of elements of the array
'''

from collections import OrderedDict

def LongestSubsetWithZeroSum(arr):

    # Map to store the previous sums
    presum = OrderedDict()

    sum = 0  # Initialize the sum of elements
    maxLen = 0  # Initialize result
    n = len(arr)

    # Traverse through the given array
    for i in range(n):
        # Add current element to sum
        sum += arr[i]

        if (arr[i] == 0 and maxLen == 0):
            maxLen = 1
        if sum == 0:
            maxLen = i + 1

        # Look for this sum in Hash table
        if (sum in presum):
            # If this sum is seen before, then update maxLen
            maxLen = max(maxLen, i - presum.get(sum))

        else:
            # Else insert this sum with index in hash table
            presum[sum] = i

    return maxLen





