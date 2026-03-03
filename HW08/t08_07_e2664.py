def sort(array, n):
    for index in range(1, n):
        flag = False
        currentValue = array[index]
        position = index
        while position > 0:
            if array[position - 1] > currentValue:
                array[position] = array[position - 1]
                flag = True
            else:
                break
            position -= 1
        array[position] = currentValue
        if flag:
            print(*array)

n = int(input())
arr = [int(x) for x in input().split()]
sort(arr, n)