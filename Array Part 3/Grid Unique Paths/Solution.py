class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
       # @lru_cache(None)
        cur=[1]*n
        for i in range(1,m):
            for j in range(1,n):
                cur[j]+=cur[j-1]
        return cur[-1]
    
# Recursive Approach
"""
    Time Complexity  : O(2 ^ (M + N)) 
    Space Complexity : O(max(M,N))
    
    Where 'M' is the number of rows and 'N' is the number of columns of the matrix.    
"""

def uniquePaths(m, n):
    
	# Base condition.
    if(m == 1 or n == 1):            
	    return 1

	# Recursive call.
    return uniquePaths(m - 1, n) + uniquePaths(m, n - 1)  

# Memoization

"""
    Time Complexity  : O(M * N) 
    Space Complexity : O(M * N)
    
    Where 'M' is the number of rows and 'N' is the number of columns of the matrix.   
"""

def uniquePathsHelper(m, n, lookupTable):

    # Base condition.
    if(m == 1 or n == 1):           
        return 1
    
    # Check for solved subproblems.
    if(lookupTable[m][n] != -1):    
        return lookupTable[m][n]

    # Recursive call.
    temp = uniquePathsHelper(m - 1, n, lookupTable) + uniquePathsHelper(m, n - 1, lookupTable)
    lookupTable[m][n] = temp
    
    return temp                  

def uniquePaths(m, n):
    
    # Lookup table.
    lookupTable = [[-1 for i in range(n+1)] for j in range(m+1)]      

    # Calling helper function.
    return uniquePathsHelper(m,n,lookupTable)           

### Dynamic Programming

"""
    Time Complexity  : O(M * N) 
    Space Complexity : O(M * N)
    
    Where 'M' is the number of rows and 'N' is the number of columns of the matrix.   
"""

def uniquePaths(m, n):

    # Reference table to store subproblems.
    dp = [[0 for i in range(n)] for j in range(m)]                  

    # Paths to reach a cell in column 1.
    for i in range(m):
        dp[i][0] = 1
    
    # Paths to reach a cell in row 1.
    for j in range(n):  
        dp[0][j] = 1
    
    # Bottom up approach.
    for i in range(1, m):  
        for j in range(1, n):  
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] 

    # Returning answer.
    return dp[m - 1][n - 1] 

###Dynamic Programming Space optimized

"""
    Time Complexity  : O(M * N) 
    Space Complexity : O(N)
    
    Where 'M' is the number of rows and 'N' is the number of columns of the matrix.   
"""

def uniquePaths(m, n):

    # Reference array to store subproblems.
    dp = [0 for i in range(n)]                  

    dp[0] = 1

    # Bottom up approach.
    for i in range(m): 

        for j in range(1, n):
            dp[j] += dp[j - 1]
        
    # Returning answer.
    return dp[n - 1]                  
