# Функция для определения пересечения, пересечение будет выведено в отдельном списке
def both(l1, l2):
    l3=[]
    l4=[]
    for i in range(len(l1)):
        for j in range(len(l2)):
            if (l2[j]==l1[i]):
                l3.append(l2[j])
    # Убирание дубликатов из списка l3 с помощью буферного временного списка l4           
    for k in l3: 
        if k not in l4: 
            l4.append(k) 
    l3 = l4
    return l3

# Два списка, которые я просто вставил для самопроверки
list1= [1, 10,'слово',115]
list2 = [10, 2,'слово',1053]
# Вызов функции
print(both(list1, list2))


# Принятие на вход двух списков
lista=[]
listb=[]

print('Первыйсписок введите: ')
for i in range(5):
    lista.append(input())
print('Следующий список введите: ')
for i in range(5):
    listb.append(input())

# Вызов функции
print(both(lista, listb))