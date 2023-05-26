print("Введите список")
def revver():
    my_list = []
    for i in range(1,5,1):
        my_list.append(input())
    my_list.sort()
    return my_list[0],my_list[1]

print(revver())