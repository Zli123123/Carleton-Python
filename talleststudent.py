import random
import time
import timeit

random.seed(time.time())

studheight = []
value1 = 0
for i in range (10):
    value1 = random.randint(40, 250)
    studheight.append (value1)
print(studheight) 

#studheight= [140, 145, 132, 167, 146, 188]

start = timeit.timeit()
talleststudent = studheight[0]
secondtallest = 0
size = len(studheight)
if studheight[0] > studheight[1]:
    talleststudent = studheight[0]
else:
    talleststudent = studheight[1]

for i in range(2, size):
    if studheight[i] > talleststudent:
        secondtallest = talleststudent
        talleststudent = studheight[i]
    elif studheight[i]>secondtallest and talleststudent != studheight[i]:
        secondtallest = studheight[i]

print("largest element: ", talleststudent)
print("second largest element: ", secondtallest)
     
end = timeit.timeit()

#tudheight.sort
#rint(studheight[1)
#rint(studheight[2)

start1 = timeit.timeit()
studheight.sort(reverse=True)
print("largest element: ", studheight[0])
print(" second largest element: ", studheight[1])
end1 = timeit.timeit()

print((end - start) *1000)
print((end1 - start1) *1000 )