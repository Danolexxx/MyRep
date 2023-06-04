import math
myList = [(1, 2), (3, 4), (-1, 5), (6, -3)]
def sortByLength(element):
    return math.dist(element, (0,0))
sortedList = sorted(myList, key=sortByLength)
print (sortedList)