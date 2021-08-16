def maxSquare(arr, num):
    arr_sorted = sorted(arr)
    max = num

    if(len(arr) < 0):
        return max
    
    for i in arr_sorted:
        if (max == i):
            max += max
    return max

arr = [1,2,4,11,12,8]
num = 2
print(maxSquare(arr, num))
    