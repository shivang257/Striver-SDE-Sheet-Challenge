class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
     #   nums.sort()
        arr=set(nums)
        mx=0
        for num in arr:
            if num-1 not in arr:
                t=0
                while (num+t) in arr:
                    t+=1
                mx=max(mx,t)
        return mx  

# BRUTE FORCE 
    
'''
    Time Complexity: O(N^3)
    Space Complexity: O(1) 

    Where N is the length of array.
'''

# To check whether currNum is present in array or not.
def arrayItContains(currNum, n, arr):
    for i in range(n):
        if (arr[i] == currNum):
            return True

    return False


def lengthOfLongestConsecutiveSequence(arr, n): 
    # To store length of longest consecutive sequence.
    mx = 0
    
    for i in range(n):
        count = 1
        
        # Making arr[i] as first element of sequence.
        currNum = arr[i]
        
        while arrayItContains(currNum + 1, n, arr):
            # Setting currNum to be next consecutive element by increament.
            currNum += 1
            count += 1
            
        # Update maximum length of consecutive sequence if any.
        mx = max(mx, count)
        
    return mx

# APPROACH - SORTING

'''
    Time Complexity: O(N*logn(N))
    Space Complexity: O(1)

    Where N is the length of array.
'''

def lengthOfLongestConsecutiveSequence(arr,n):
    
   # Sort the given array in ascending order.
   arr.sort()
    
   # To store length of longest consecutive sequence.
   mx = 0
    
   # To store the length of current consecutive Sequence.
   count = 0
   
   for i in range(n):
        
        # Check if previous value is consecutive to the current value.
        if (i > 0 and  (arr[i] == arr[i - 1] + 1)):
            
            count += 1
        
        # Skip if the current value is equals to the previous value.
        elif (i > 0 and  arr[i] == arr[i - 1]):
                continue
                
        # Reseting count for next upcoming consecutive sequence.
        else:
            count = 1
            
        mx = max(mx,count)
        
   return mx


# USING HASH TABLE
 '''  
    Time Complexity: O(N)
    Space Complexity: O(N)

    Where N is the length of the given array.
'''

def lengthOfLongestConsecutiveSequence(arr, n):
    # To store length of longest consecutive sequence.
    mx = 0
    
    # To store the length of current consecutive Sequence.
    count = 0
    
    # To store all the unique elements of array.
    sett = set()
    
    for element in arr:
        sett.add(element)
        
    for element in arr:
        
        previousConsecutiveElement=element-1
        
        if(not previousConsecutiveElement in sett):
            
            # Element is the first value of consecutive sequence.
            j = element
            
            while j in sett:
                
                # The next consecutive element by will be j + 1.
                j += 1
            
            # Update maximum length of consecutive subsequence.
            mx = max(mx , j-element)
     
    return mx