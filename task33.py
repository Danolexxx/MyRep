my_list = []
ans=input()
def counter(slovo,count):
    my_newlist = []
    for i in range(0, len(slovo), 1):
        my_list.append(slovo[i])
        my_newlist.append(slovo[i])
    for j in range(0, len(slovo), 1):
        for k in range(0, len(slovo), 1):
            if (my_list[k]==my_list[j]) and (j!=k):
                count=count+1
                my_list[j]=0
                my_newlist.pop()
            elif (count>0):
                my_newlist[k]=count
                count=0
    return my_newlist

print(counter(ans,0))
