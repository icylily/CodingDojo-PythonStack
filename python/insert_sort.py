def innsert_sort(arr):
    count = len(arr)
    for i in range(1,count):
        key = arr[i]
        # print(key)
        j = i-1
        while j>=0:
            if (arr[j]>key):
                arr[j+1]=arr[j]
                arr[j]=key
            j-=1
    return arr
print(innsert_sort([0,3,5,7,8,2,-6]))

