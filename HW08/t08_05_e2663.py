def sortCounter(array, n):
    counter = 0
    for i in range(0, n):
        for j in range(0, n-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                counter+=1
    return counter

n = int(input())
arr = [int(x) for x in input().split()]
print(sortCounter(arr, n))