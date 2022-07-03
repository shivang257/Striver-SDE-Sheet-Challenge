# Solution Approach - 1: 
# Easy Approach

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for i in range(numRows):
            row=[1]*(i+1)
            for j in range(1,i):
                row[j]=ans[i-1][j]+ans[i-1][j-1]
            ans.append(row)
        return ans

# Solution - 2 :

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]
        for i in range(numRows-1):
            temp=[0]+ans[-1]+[0]
            row=[]
            for j in range(len(temp)-1):
                row.append(temp[j]+temp[j+1])
            ans.append(row)
        return ans
    
    