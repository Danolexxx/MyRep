my_list = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
ans=input()
def revver(slovo, count):
    my_newlist = []
    for i in range(1, len(slovo), 1):
        my_newlist.append(slovo[i])
    for k in range(0, 10, 1):
            count=count+my_newlist.count(my_list[k])
    return count

print("гласные - ", revver(ans, 0))
print("согласные - ", len(ans)-revver(ans, 0))