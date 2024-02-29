import math
import matplotlib.pyplot as plt

tick = 0.001
roop = 100
history = []

class star() :
    def __init__(self,x,y,math,speed_x,speed_y) :
        self.x = x
        self.y = y
        self.math = math
        self.speed_x = speed_x
        self.speed_y = speed_y

A = star(-1,0,1,0,1)
B = star(1,0,2,0,-1)

distance = math.sqrt((A.x-B.x)**2 + (A.y-B.y)**2)

def move() :
    AtoB_x = B.x - A.x
    AtoB_y = B.y - A.y
    BtoA_x = A.x - B.x
    BtoA_y = A.y - B.y
    A.x = A.x + (A.speed_x + AtoB_x * B.math / distance ** 2) * tick
    A.y = A.y + (A.speed_y + AtoB_y * B.math / distance ** 2) * tick
    B.x = B.x + (B.speed_x + BtoA_x * A.math / distance ** 2) * tick
    B.y = B.y + (B.speed_y + BtoA_y * A.math / distance ** 2) * tick


k = 0
while k < roop :
    history.append([[A.x,A.y],[B.x,B.y]])
    plt.plot((A.x,B.x),(A.y,B.y),".")
    move()
    k += 1


print(A.x,A.y)
print(B.x,B.y)
print(history)
