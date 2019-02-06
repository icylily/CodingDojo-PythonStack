for x in range(0, 151):
    print(x)
# output: 0, 1,2,3...150

for x in range(5,1001,5):
    print(x)

for x in range(1,101):
    if(x %10 == 0):
        print("Coding Dojo")
    elif(x %5==0):
        print("Coding ")
    else:
        print(x)
sum = 0
for x in range(1,500000,2):
    sum +=x
print(sum)

for x in range(2018,0,-4):
    print(x)

def flexible_counting(lowNum,highNuum,mult):
    while (lowNum <= highNuum):
        if (lowNum % mult == 0):
            print(lowNum,end=" ")
            lowNum += mult
        else:
            lowNum+=1
    return 0    
flexible_counting(2,9,3)
