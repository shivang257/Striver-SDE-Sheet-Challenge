def getInversions(arr, n) :
    a=0
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i]>arr[j]):
                a+=1
    return a