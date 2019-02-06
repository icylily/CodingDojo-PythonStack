def countdown(x):
    list=[]
    for i in range(x,-1,-1):
        list.append(i)
    return list
print(countdown(5))


def print_and_return(list):
    print(list[0])
    return list[1]
print(print_and_return([1,2]))


def first_plus_length(list):
    print(list[0])
    print(len(list))
    return list[0] + len(list)


print(first_plus_length([1, 2, 3, 4, 5]))


def values_greater_than_second(list):
    if len(list)<2:
        return False
    newlist = []
    for x in range(len(list)):
        if(list[x]>list[1]):
            newlist.append(list[x])
    print(len(newlist))
    return newlist


print(values_greater_than_second([5, 2, 3, 2, 1, 4]))


def length_and_value(theLength,theValue):
    newlist = []
    for x in range(theLength):
        newlist.append(theValue)
    return newlist
print(length_and_value(4,7))
print(length_and_value(6,2))
