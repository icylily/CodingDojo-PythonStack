def select_sor(arr):
    count = len(arr)
    for i in range(count):
        min = i
        for j in range(i+1,count):
            if arr[min]>arr[j]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr
print(select_sor([7,4,9,3,12,2,1,6]))

