class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major=0
        count=0
        for num in nums:
            if count==0:
                major=num
            if major==num:
                count+=1
            else:
                count-=1
        return major
    
##Brute Force Approach

    
'''
    Time Complexity: O(N ^ 2)
    Space Complexity: O(1)

    Where 'N' is the size of array/list.
'''

def findMajorityElement(arr, n):
	# Iterating each element in the array/list and check if it is a majority element.
	for i in range(n):	
		# Variable to store the frequency of the current element at index 'i'.
		maxCount = 0

		# Iterating the array/list to count the frequency of the current element at index 'i'.
		for j in range(n):
			# Increment the count of variable if an occurrence of the current element is observed.
			if arr[j] == arr[i]:
				maxCount += 1

		# If count of any element exceeds 'n' / 2, then it is the majority element.
		if maxCount > n/2:
			return arr[i]
		
	# If no majority element found, return -1.
	return -1