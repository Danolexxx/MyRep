my_list = [5, 7, 11, 13, 15, 20, 25]
new_list = []
for i in my_list:
    if (i > 10):
        new_list.append(i)

print(sum(new_list)/len(new_list))