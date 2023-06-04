my_list = []
def WRote(a):
    print(a)
    print(min(a))
i=5
try:
    for i in range(1,6,1):
        my_list.append(input())
        if (type(int(my_list[i-1]))!=int):
            exit
    WRote(my_list)
except ValueError:
    print('не целое')
    exit