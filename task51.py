list1 = [24, 36, 48, 60]
list2 = [12, 18, 24, 36, 72]
list1.extend(list2)
def NOD(a,b):
    while (a!=b):
        if a<b:
            b=b-a
        else:
            a=a-b
    for i in range(1,len(list1),1):
        if (list1[i]%a!=0):
            NOD(min(list1),list1[i])
        else:
            return a
print(NOD(min(list1),max(list1)))