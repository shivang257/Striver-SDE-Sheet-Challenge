## BRUTE FORCE

'''
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    
    Where N is the size of the array.
'''

def reversePairs(arr, n):
    
    ans = 0
    
    # Iterate i from 0 to n
    for i in range(n):

        # Iterate j from 0 to i
        for j in range(i):
            
            if arr[j] > arr[i] * 2:
                ans += 1
    
    return ans

## Modified Merge-Sort


'''

    Time Complexity: O(N * log(N))
    Space Complexity: O(N)
    
    Where N is the size of the array.
    
'''

def merge(arr, start, mid, end):
    
    # Merging the arrays using helper arrays
    n1 = (mid - start) + 1
    n2 = end - mid
    left = [0] * n1
    right = [0] * n2
    
    for i in range(n1):
        left[i] = arr[start + i]
        
    for j in range(n2):
        right[j] = arr[mid + 1 + j]
        
    i, j = 0, 0
    
    for k in range(start, end + 1):
        if j >= n2 or (i < n1 and left[i] <= right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

def mergeSort(arr, start, end):
    if start < end:
        mid = (start + end)//2
        
        # Counting the pairs in the left and right subarrays.
        count = mergeSort(arr, start, mid) + mergeSort(arr, mid + 1, end)
        j = mid + 1
        
        for i in range(start, mid + 1):
            while j <= end and arr[i] > arr[j] * 2:
                j += 1
            count += j - (mid + 1)
        
        # Merging the arrays.
        merge(arr, start, mid, end)
        return count 
    
    else:
        return 0

def reversePairs(arr, n):
    return mergeSort(arr, 0, n - 1)

