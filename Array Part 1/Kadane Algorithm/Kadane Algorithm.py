#Solution Number - 1 :
 

def maxSubarraySum(arr, n) :
    m1=arr[0]
    m2=0
    for i in range(len(arr)):
        m2=m2+arr[i]
        if m2<0:
            m2=0
        elif m1<m2:
            m1=m2
    if m1<0:
        return 0
    return m1
    


# Solution Number - 2 ;

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m1=nums[0]
        m2=nums[0]
        for i in range(1,len(nums)):
            m1=max(nums[i],m1+nums[i])
            m2=max(m1,m2)
        return m2






