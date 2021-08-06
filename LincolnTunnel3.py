import math
import random
from graphics import *
import time


class Car :
    
    def __init__(self, win, id, speed, accel, h, l) :
        self._win = win
        self._id = id;
        self._size = l  # default car size 3 meters
        self._h = h
        
        self._vOrig = self._v = speed
        
        self._x = 0
        self._a = accel
        
        self._xNew = 0
        self._vNew = 0
        self._aNew = 0
        
        # *** INITIAL DRAWING ***
        #draw green circle
        self._cir = Circle(Point(40,100), self._size * 3)
        self._cir.setFill("lightgreen")
        self._cir.draw(win)
        
        # draw cad ID
        self._label = Text(Point(40, 100), str(self._id))
        self._label.draw(win)       
              
    
    def __str__(self) :
        return 'ID = ' + str(self._id) + '  X = '+ str(self._x) + '  V = ' + str(self._v) + '  A = ' + str(self._a) 
                                                                                                                            
    
    # getters
    def getID(self) -> int :
        return self._id
    
    def getX(self) -> float :
        return self._x;
    
    def getSize(self) :
        return self._size
    
    def isBreaking(self) :
        if self._a == 0 :
            return False
        else :
            return True
    
    # main simulation functions
    
    def step(self, curTime, tau) :

        self._vNew = self._v + self._a*tau
        
        # prevent uncontrollable acceleration
        if self._a > 0 and self._vNew >= self._vOrig :
            self._aNew = 0
            
        # prevent bogus reverse    
        if self._a <= 0 and self._vNew <= 0 :
            self._vNew = 0
            self._aNew = 0
            
        self._xNew = self._x + self._v*tau + self._a*tau*tau/2
        
    def update(self) :

        self._a = self._aNew
        self._v = self._vNew
        self._x = self._xNew
        
    def draw(self) :
        xOffset = self._xNew - self._x
        #---print(xOffset)
        if self._a < 0 :
            self._cir.setFill('red')
        elif self._a > 0 :
            self._cir.setFill('yellow')
        self._cir.move(int(xOffset)/2, 0)
        self._label.move(int(xOffset)/2, 0)
        
    # cleaning car sprite from the screen by moving it outside of the window
    def removeDraw(self) :
        xOffset = 5000
        self._cir.move(int(xOffset)/2, 0)
        self._label.move(int(xOffset)/2, 0)
    
    # driver's brain :)     
    def drivingControl(self, d, prevBreaking) :
        if d > 4*self._size :
            # resume original speed
            if self._v < self._vOrig :
                self._aNew = 0.5 # re-acceleration afte slow down
        else :
            if prevBreaking :
                self._aNew = -5 # emergency breaking
            else :
                self._aNew = -2.5 # regular breaking
        
    
if __name__ == '__main__' :
    
    def isCollision(car, prevCar) :
        carSize = 3
        return prevCar != None and abs(car.getX()-prevCar.getX()) < carSize
        
    win = GraphWin('Traffic Simulator v 0.4', 1200, 250)    
    
    # system initialization
    random.seed() 
    
    MAX_CAR = 99
    TUNNEL_LEN = 2250
    TAU = 1   # simulation step 1 sec
    
    cars = []
    
    # simulate car group strolling through the tunnel
    iCar = 0
    simTime = 0
    nextCarInterval = 0
    curCarInterval = 0
    carCollision = False
    
    while True :
        
        print('\n*** time =', simTime)
        time.sleep(0.1)
        
        if curCarInterval == nextCarInterval :# time to generate a new car
            # create a new car
            nextCar = Car(win, iCar, random.randint(12, 16), random.randint(0, 2), 5, random.randint(3, 5))
            #print(nextCar)
            cars.append(nextCar) # car speed is a random number between 12 and 19 m/sec    
            # generate rabdom interval to the next car
            nextCarInterval = random.randrange(7, 12)
            curCarInterval = 0
            iCar += 1
            if iCar > MAX_CAR :
                break
        else :
            curCarInterval += 1
            
        # car animation sequence
        prevCar = None
        count = 0
        for curCar in cars :
            
            #---print(curCar)
            distNextCar = -1
            if prevCar != None :
                distNextCar = prevCar.getX() - curCar.getX() 
                curCar.drivingControl(distNextCar, prevCar.isBreaking())
            #---print('distance to next car is', distNextCar)
            curCar.step(simTime, TAU)
            
            # check traffic conditions
            # 1. Car left tunnel :)
            if curCar.getX() > TUNNEL_LEN :
                curCar.removeDraw() # remove car sign from GUI
                cars.remove(curCar) # remove car from simulator
            # 2. Car collision check  
            if isCollision(curCar, prevCar) :
                carCollision = True
                print('!!! Car collision between', curCar.getID(), prevCar.getID())
                break
            
            prevCar = curCar
            
        if carCollision :
            break;
        if len(cars) == 0 : # all car left tunnel
            break
    
        # car parameters update: current <- new
        for curCar in cars :
            curCar.draw()
            curCar.update()

        count += 1
        simTime += TAU    #increment simulation time
        
    print('\n****  Simulation is over  ****')
    
        
                
        
        
    
    
        