import random
print("Введите строку")
ans=input()
def revver(slovo):
    my_list = []
    for i in range(len(slovo)-1, -1,-1):
        my_list.append(slovo[i])
    my_list="".join(my_list)
    return my_list

print(revver(ans))