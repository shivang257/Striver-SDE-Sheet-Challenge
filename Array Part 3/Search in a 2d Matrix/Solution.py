class Solution:
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None:
            return False
        row,col=len(matrix),len(matrix[0])
        low,high=0,row*col-1
        while(low<=high):
            mid=(low+high)//2
            num=matrix[mid//col][mid%col]
            if num==target:
                return True
            elif(num<target):
                low=mid+1
            else:
                high=mid-1
        return False
    
### Brute Force

'''
    Time Complexity: O(M*N)
    Space Complexity: O(1)

    Where M and N are the number of rows and columns.
'''


def findTargetInMatrix(mat, m, n, target):

    for i in range(m):
        for j in range(n):

            if mat[i][j] == target:
                return True

    return False


## Binary Search

'''
    Time Complexity: O(log(M*N))
    Space Complexity: O(1)

    Where M and N are the number of rows and columns.
'''


def findTargetInMatrix(mat, m, n, target):

    start, end = 0, m * n - 1

    # Binary search.
    while start <= end:
        
        mid = start + (end - start) // 2
        val = mat[mid // n][mid % n]

        if target < val:
            end = mid - 1

        elif target > val:
            start = mid + 1

        else:
            return True

    return False