# Solution - 1 
#Time Complexity : O(N)
#Space Complexity : O(1)
#Best Optimum Solution For This Problem

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row,col=len(matrix),len(matrix[0])
        r=False
        
        #determine which row or column need to be zero
        for i in range(row):
            for j in range(col):
                if(matrix[i][j]==0):
                    matrix[0][j]=0
                    if i>0:
                        matrix[i][0]=0
                    else:
                        r=True
                        
        # zero most of them by making zero all the corresponding row and column
        for i in range(1,row):
            for j in range(1,col):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
        # if first row first column is zero
        if matrix[0][0]==0:
            for i in range(row):
                matrix[i][0]=0
        if
        if(r):
            for i in range(col):
                matrix[0][i]=0