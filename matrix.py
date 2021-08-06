import random 
import time
random.seed(time.time())
yaxis = 3
xaxis = 3
print("5 1 2")
print("1 0 3")
print("2 3 5")
listwhole = [5, 1, 2, 1, 0, 3, 2, 3, 5]
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
try1 = 0
for i in range (0, len(listwhole)):
    try1 = 0
    for k in range(0, len(listy)):
        if listx[i] == listy[k] and listy[i] == listx[k]:
            pointcomp2 = listwhole[k]
            pointcomp = listwhole[i] 
            if pointcomp == pointcomp2:
                print("__")
                print ("k: ", k, "i:", i)
                print(listwhole[k], "=", listwhole[i], "yes")
                print(listx[i], ",", listy[i], "--", listx[k], ",", listy[k])
                break
        else:
            try1 += 1

                
        if try1 == 9:
            countcount += 1
            print("__")
            print(listx[i], ",", listy[i], "--", listx[k], ",", listy[k])
            print("no")                

if countcount == 0:
    print("ANSWER: SYMMETRICAL")
else:
    print("ANSWER: NOT SYMMETRICAL")