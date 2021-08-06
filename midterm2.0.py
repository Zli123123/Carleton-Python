import turtle
import random
import time
screen = turtle.Screen()
random.seed(time.time())
turtle.setup( width = 1700, height = 700)
#____________________
t = turtle.Turtle() 
t.penup()
t.goto(700, 250)
t.right(90)
t.pendown()
t.pencolor("blue")
t.forward(500)
t.right(90)
t.forward(600)
t.right(90)
t.forward(500)
t.right(90)
t.forward(600)
time.sleep(3)


listx = []
listy = []
listx2 = []
listy2 = []     
originx = 0
originy = 0


for i in range(50): 
    uniqueFlag = False
    while not uniqueFlag :
        
        uniqueFlag = True
        x = random.randint(101, 700)
        x2 = x + random.randint(20, 50)
        y = random.randint(-249, 249)
        y2 = y + random.randint(15, 40)
        originx = (x + x2) / 2
        originy = (y + y2) / 2
        for j in range(i) :
            if x2 > 700:
                uniqueFlag = False
                break
            elif y2 > 250:
                uniqueFlag = False
                break
            elif (x >= listx[j] and x <= listx2[j]) and (y >= listy[j] and y <= listy2[j]):
                uniqueFlag = False
                break
            elif (x >= listx[j] and x <= listx2[j]) and (y2 >= listy[j] and y2 <= listy2[j]):
                uniqueFlag = False
                break
            elif (x2 >= listx[j] and x2 <= listx2[j]) and (y2 >= listy[j] and y2 <= listy2[j]):
                uniqueFlag = False
                break
            elif (x2 >= listx[j] and x2 <= listx2[j]) and (y >= listy[j] and y <= listy2[j]):
                uniqueFlag = False
                break            
            elif (originx >= listx[j] and originx <= listx2[j]) and (originy >= listy[j] and originy <= listy2[j]):
                uniqueFlag = False
                break
            elif (originx >= listx[j] and originx <= listx2[j]) and (y >= listy[j] and y <= listy2[j]):
                uniqueFlag = False
                break
            elif (originx >= listx[j] and originx <= listx2[j]) and (y2 >= listy[j] and y2 <= listy2[j]):
                uniqueFlag = False
                break            
            elif (x >= listx[j] and x <= listx2[j]) and (originy >= listy[j] and originy <= listy2[j]):
                uniqueFlag = False
                break            
            elif (x2 >= listx[j] and x2 <= listx2[j]) and (originy >= listy[j] and originy <= listy2[j]):
                uniqueFlag = False
                break            
        if uniqueFlag == True:      
            listx.append(x)
            listy.append(y)
            listx2.append(x2)
            listy2.append(y2)

for i in range(50):
    t.penup()
    t.goto(listx[i], listy[i])
    t.pendown()
    t.pencolor("red")
    t.goto(listx[i], listy2[i])
    t.goto(listx2[i], listy2[i])
    t.goto(listx2[i], listy[i])
    t.goto(listx[i], listy[i])
time.sleep(5)
            
            
    
    
