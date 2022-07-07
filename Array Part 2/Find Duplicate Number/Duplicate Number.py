class Solution:
    def findDuplicate(self, arr: List[int]) -> int:
        arr.sort()
        for i in range(len(arr)-1):
            if(arr[i]==arr[i+1]):
                return arr[i]