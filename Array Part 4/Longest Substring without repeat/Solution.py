class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        start,output=-1,0
        for i,j in enumerate(s):
            if j in seen:
                if(seen[s[i]]>start):
                    start=seen[s[i]]
            seen[s[i]]=i
            output=max(output,i-start)
        return output 
    
# All Substring Approach
    
''''
    Time Complexity - O(N^3)
    Space Complexity - O(N)

    where N is the length of the string.
'''

def allUnique(wrapper, start, end) :

    # for storing every character of string
    Set = set()
    for i in range(start, end) :
        ch = wrapper[0][i]

        # if a character is already there then we have a found duplicates
        # so we need to return false
        if ch in Set :
            return False
        
        Set.add(ch)

    return True

def uniqueSubstrings(input) :

    n = len(input)
    ans = 0

    # check for every possible substring
    # creating the wrapper around the string 
    # so that on every function call string is not copied
    wrapper = []
    wrapper.append(input)
    for i in range(n) :
        for j in range(i+1, n+1) :
            
            # if substring contains unique characters then update the maximum.
            if (allUnique(wrapper, i, j)) :
                ans = max(ans, j - i)
            
    return ans


# USING SLIDING WINDOW APPROACH

''''
    Time Complexity - O(N)
    Space Complexity - O(K)

    where N is the length of the string.
    and K in number of different character in the string 
'''


def uniqueSubstrings(input) :

    n = len(input)
    Set = set()

    ans = 0
    i = 0
    j = 0

    while(i < n and j < n) :
        
        # try to extend the range [i,j]
        if input[j] not in Set :

            Set.add(input[j])
            ans = max(ans, j - i + 1)
            j+=1
        
        else :
            Set.remove(input[i])
            i+=1

    return ans

