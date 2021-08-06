#captcha
import turtle
import random
import time

t = turtle.Turtle()
#if this letter, then do this
#random line length
#random distance between letters
value1 = random.randint(1, 26)
def letters(s):
    scale = 4
    if s == 0:
        turtle.down ( )
        # Point upwards to begin
        turtle.left ( turtle.heading ( ) + 90 )
        turtle.right ( 20 )
        turtle.forward ( 10 * scale )
        turtle.right ( 70 )
        turtle.forward ( 1 * scale )
        turtle.right ( 70 )
        turtle.forward ( 10 * scale )
        turtle.backward ( 5 * scale )
        turtle.right ( 90 + 20 )
        turtle.forward ( 5 * scale )
        #Move to right of letter and over 1 * scale
        turtle.up ( )
        turtle.backward ( 5 * scale )
        turtle.left ( 110 )
        turtle.forward ( 5 * scale )
        turtle.left ( 70 )
        turtle.forward ( 1 * scale )  
    if s == 1:
        turtle.down ( )
        # Point upwards to begin
        turtle.left ( turtle.heading ( ) + 90 )
        turtle.forward ( 10 * scale )
        turtle.right ( 90 )
        turtle.forward ( 4 * scale )
        turtle.right ( 90 )
        turtle.forward ( 4 * scale )
        turtle.left ( 90 )
        turtle.backward ( 1 * scale )
        turtle.forward ( 2 * scale )
        turtle.right ( 90 )
        turtle.forward ( 6 * scale )
        turtle.right ( 90 )
        turtle.forward ( 5 * scale )
        # Move to right of letter
        turtle.up ( )
        turtle.right ( 180 )
        turtle.forward ( 6 * scale )
    if s == 2:
        turtle.down ( )
        # Point upwards to begin
        turtle.left ( turtle.heading ( ) + 90 )
        turtle.forward ( 10 * scale )
        turtle.right ( 90 )
        turtle.forward ( 4 * scale )
        turtle.backward ( 4 * scale )
        turtle.left ( 90 )
        turtle.backward ( 10 * scale )
        turtle.right ( 90 )
        turtle.forward ( 4 * scale )
        # Move to right of letter
        turtle.up ( )
        turtle.forward ( 1 * scale )
    if s == 3:
        turtle.down ()
        turtle.left ( turtle.heading ( ) + 90 )
        turtle.forward (scale*10)
        turtle.right(90)
        turtle.forward(scale*5)
        turtle.right(90)
        turtle.forward(scale*10)
        turtle.right(90)
        turtle.forward(scale*5)
        turtle.up ( )
        turtle.right(180)
        turtle.forward ( 6 * scale )        
    if s == 4:
        turtle.down()
        turtle.left ( turtle.heading ( ) + 90 )
        turtle.forward (scale*10)
        turtle.right(90)
        turtle.forward(2*scale)
        turtle.right(35)
        turtle.forward(2*scale)
        turtle.right(55)
        turtle.forward(scale*7.8)
        turtle.right(55)
        turtle.forward(2*scale)
        turtle.right(35)
        turtle.forward(scale*2)
        turtle.up ( )
        turtle.right(180)
        turtle.forward ( 5 * scale )        
    #if s == 5:                
    #if s == 3:
    #if s == 3:
    #if s == 3:
list = []
list2 = ["A", "B", "C", "O", "D"]
for i in range(6):
    b = random.randint(0,4)
    list.append(list2[b])
    letters(b)
time. sleep(3)
turtle.bye()

correct = 0
inp = input("captcha: ")
for i in range( len(inp) ):
    if inp[i] == list[i]:
        correct += 1
if correct == 6:
    print("Not a robot, authorized")
else:
    print("You are a robot")

