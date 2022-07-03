# Solution 1 :  Counting Sort
# Time Complexity: O(N)+O(N)
# Space Complexity: O(1)

def sort012(arr, n) :
    c1=0
    c2=0
    c3=0
    for i in range(len(arr)):
        if(arr[i]==0):
            c1+=1
        elif(arr[i]==1):
            c2+=1
        else:
            c3+=1
    for i in range(c1):
        arr[i]=0
    for i in range(c1,c1+c2):
        arr[i]=1
    for i in range(c1+c2,len(arr)):
        arr[i]=2


# Solution - 2 : Using Left and Right Swapping 
# Time Complexity: O(N)
# Space Complexity: O(1)


def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r=0,len(nums)-1
        i=0
        while i<=r:
            if(nums[i]==0):
                nums[l],nums[i]=nums[i],nums[l]
                l+=1
            elif(nums[i]==2):
                nums[i],nums[r]=nums[r],nums[i]
                r-=1
                i-=1
            i+=1

# Solution - 3 : Using Dutch National Flag Algorithm

class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,mid,h=0,0,len(arr)-1
        while(mid<=h):
            if(arr[mid]==0):
                arr[l],arr[mid]=arr[mid],arr[l]
                l+=1
                mid+=1
            elif(arr[mid]==2):
                arr[h],arr[mid]=arr[mid],arr[h]
                h-=1
            else:
                mid+=1