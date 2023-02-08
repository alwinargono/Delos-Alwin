def sameOrNot(arr, n):
    if arr[0] == arr[n-1]:
        return "YES"
    for i in range(1, n):
        left = sum(arr[0:i])
        right = sum(arr[i+1:])
        if(left == right):
            return "YES"
    return "NO"
 
arr = [0,2,0,0]
length = len(arr)
print(sameOrNot(arr,length))

