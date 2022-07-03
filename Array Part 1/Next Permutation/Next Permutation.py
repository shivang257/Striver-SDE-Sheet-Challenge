# Solution - 1:
# In this problem we have focused on the pattern of the output

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx1=0
        idx2=0
        for i in range(len(nums)-1,-1,-1):        
            if nums[i-1]<nums[i]:
                idx1=i-1
                break
        if idx+1!=0 :
            for j in range(len(nums)-1,-1,-1):
                if nums[j]>nums[idx1]:
                    idx2=j
                    break 
            nums[idx1],nums[idx2]= nums[idx2],nums[idx1]
        nums[idx+1:]=reversed(nums[idx1+1:])