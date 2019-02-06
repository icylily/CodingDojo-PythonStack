def biggie_size(list):
    for x in range(len(list)):
        if (list[x] > 0):
            list[x]='big'
    print(list)
    return list
biggie_size([-1, 3, 5, -5]) 


def count_positives(list):
    sum_positvies = 0
    for x in range(len(list)):
        if (list[x]>0):
            sum_positvies +=1
    list[-1] = sum_positvies
    return list


print(count_positives([-1, 1, 1, 1]))
print( count_positives([1,6,-4,-2,-7,-2]) )

def sum_total(list):
    if (len(list)==0):
        return False
    sum = list[0]
    for x in range(1,len(list)):
        sum += list[x]
    return sum
print(sum_total([1,2,3,4]))    
print(sum_total([6,3,-2]))


def average(list):
    if (len(list) == 0):
        return False
    ave = sum_total(list)/len(list)
    return ave
print(average([1,2,3,4]) )


def length(list):
    return len(list)
print(length([]))


def minimum(list):
    if(len(list)==0):
        return False
    min = list[0]
    for x in range(len(list)):
        if(list[x]<min):
            min = list[x]
    return min

def maximum(list):
    if(len(list) == 0):
        return False
    max = list[0]
    for x in range(len(list)):
        if(list[x] > max):
            max = list[x]
    return max


print(maximum([37, 2, 1, -9]))
print(maximum([]))

def ultimate_analysis(list):
    if (len(list)==0):
        return False
    sum_total= min=max=ave=list[0]
    for x in range(1,len(list)):
        sum_total+=list[x]
        if(list[x]<min):
            min = list[x]
        elif(list[x]>max):
            max = list[x]
    ave = sum_total/len(list)
    analysis={}
    analysis['sumTotal'] = sum_total
    analysis['average'] = ave
    analysis['minimum'] = min
    analysis['maximum'] = max
    return analysis


print(ultimate_analysis([37, 2, 1, -9]))

def reverse_list(list):
    if(len(list)==0):
        return False
    for x in range(len(list)//2):
        tmp = list[x]
        list[x]=list[len(list)-1-x]
        list[len(list)-1-x] = tmp
    return list


print(reverse_list([37, 2, 1, -9]))










