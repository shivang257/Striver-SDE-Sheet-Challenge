# BRUTE FORCE

#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    Time Complexity : O(N ^ 2)
    Space Complexity : O(1)
    
    Where 'N' denotes the number of elements in the given array.
'''


def subarraysXor(arr, x):

    n = len(arr)
    ans = 0

    # Traverse through each subarray

    for i in range(n):

        # The variable currentXor stores the XOR of the current subarray

        currentXor = 0

        for j in range(i, n):

            currentXor = currentXor ^ arr[j]

            # Check if currentXor is equal to x

            if currentXor == x:
                ans += 1

    # Return the variable ans

    return ans


# HASHMAP

'''
    Time Complexity : O(N)
    Space Complexity : O(N)
    
    Where 'N' denotes the number of elements in the given array.
'''

def subarraysXor(arr, x):

    n = len(arr)

    # To store the prefix XOR's.
    prefXor = {}

    ans = 0

    # To keep track of the current xor.
    currXor = 0

    # Intialy Xor is 0.
    prefXor[0] = 1

    for i in range(n):

        # Update the Xor of the current prefix.
        currXor = currXor ^ arr[i]

        # Required value of the prefix Xor to make the xor of the subarray equal to X.
        req = x ^ currXor

        if( req in prefXor):

            # Add the count of prefix arrays with required xor.
            ans += prefXor[req]

        if(currXor in prefXor):        
            prefXor[currXor] = prefXor[currXor] + 1
        
        else: 
            prefXor[currXor] = 1

    return ans