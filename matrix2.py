import random 
import time
random.seed(time.time())
yaxis = 3
xaxis = 3
print("1 0 0")
print("0 8 0")
print("0 0 4")
listwhole = [1, 0, 0, 0, 8, 0, 0, 0, 4]
listx = []
listy = []


print (listwhole)    

d = 0
count = 0
count1 = 1
while d < (yaxis * xaxis):
    d += 1
    if count == xaxis:
        count = 0
        count1 += 1
    count += 1
    listy.append(count1)
    listx.append(count)
print(listx)
print(listy)
pointcomp = listwhole[0]
pointcomp2 = listwhole[0]
countcount = 0
for i in range (0, len(listwhole)):
    print("___")
    print(listwhole[i])
    if listwhole[i] !=0:
        if listx[i] == listy[i]:
            print(listx[i], "==", listy[i])
        else:
            countcount += 1
            print(listx[i], "!!!=", listy[i]) 

if countcount == 0:
    print("ANSWER: DIAGONAL")
else:
    print("ANSWER: NOT DIAGONAL")
    