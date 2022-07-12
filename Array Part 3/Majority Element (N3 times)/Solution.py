class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m1,m2,c1,c2=0,0,0,0
        l=[]
        for n in nums:
            if(m1==n):
                c1+=1
            elif(m2==n):
                c2+=1
            elif(c1==0):
                m1=n
                c1+=1
            elif(c2==0):
                m2=n
                c2+=1
            else:
                c1-=1
                c2-=1
        x,y=0,0
        for i in range(len(nums)):
            if(nums[i]==m1):
                x+=1
            if(nums[i]==m2):
                y+=1
        if(x>len(nums)//3):
            l.append(m1)
        if(y>len(nums)//3):
            l.append(m2)
        return set(l)    
    
    
# Brute Force

'''
    Time Complexity: O(N^2)
    Space Complexity: O(1)

    Where 'N' is the number of elements in the given array/list.
'''

def majorityElementII(arr):
    
    n = len(arr)
    
    # Array for storing final answer.
    majorityElement = []
    
    # Iterate through the array.
    for i in range(n):
        # Variable for storing the frequency of the current element.
        count = 0
        # Iterate through the array to find the frequency of the current element.
        for j in range(n):
            # Increment count if we find a element with value equal to current element.
            if arr[i] == arr[j]:
                
                count += 1
            
        # Include the current element in the answer if count is greater than n/3.
        if count > (n // 3) and (len(majorityElement) == 0 or (len(majorityElement) != 2 and majorityElement[-1] != arr[i])):
            majorityElement.append(arr[i])
            
    # Return all the stored majority elements.
    return majorityElement

### Sotinr Approach

'''
    Time Complexity: O(N * log(N))
    Space Complexity: O(log(N))

    Where 'N' is the number of elements in the given array/list.
'''

def majorityElementII(arr):
    
    n = len(arr)
    sm = 0
    
    # Sort the given array in non-decreasing order.
    arr.sort()
    
    # Array for storing final answer.
    majorityElement = []
    
    # Iterate through the array.
    for i in range(n):
        
        for j in range(3):
            
            sm = (sm + arr[0]) % 10
        
        # Variable for storing the frequency of the current element.
        count = 1
        x = arr[i]
        
        # Iterate while the next element is equal to the current element.
        while ((i + 1) < n) and (arr[i + 1] == x):
            
            i += 1
            count += 1
            
        # Include the current element in the answer if count is greater than n/3.
        if count > (n // 3) and arr[i] not in majorityElement:
            majorityElement.append(arr[i])
            
    # Return all the stored majority elements.
    return majorityElement