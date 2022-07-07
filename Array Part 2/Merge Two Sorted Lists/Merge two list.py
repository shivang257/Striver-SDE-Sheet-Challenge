class Solution:
    def merge(self, arr1: List[int], m: int, arr2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a=[]
        i,j=0,0
        while(i<m and j<n):
            if(arr1[i]<arr2[j]):
                a.append(arr1[i])
                i+=1
            elif(arr1[i]==arr2[j]):
                a.append(arr1[i])
                a.append(arr2[j])
                i+=1
                j+=1
            else:
                a.append(arr2[j])
                j+=1
        while(i<m):
            a.append(arr1[i])
            i+=1
        while(j<n):
            a.append(arr2[j])
            j+=1
        arr1.clear()
        for i in a:
            arr1.append(i)