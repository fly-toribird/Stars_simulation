import math
import matplotlib.pyplot as plt

tick = 60*60*24*365
roop = 10000
history = []
G = 1 #6.67428 * (10 ** -11)

class star() :
    """math:kg distance:m"""
    def __init__(self,x,y,math,speed_x,speed_y) :
        self.x = x
        self.y = y
        self.math = math
        self.speed_x = speed_x
        self.speed_y = speed_y

A = star(-100000000,0,1 * 10^24,0,0)
B = star(100000000,0,2 * 10^24,0,0)

distance = math.sqrt((A.x-B.x)**2 + (A.y-B.y)**2)

def move() :
    AtoB_x = B.x - A.x
    AtoB_y = B.y - A.y
    BtoA_x = A.x - B.x
    BtoA_y = A.y - B.y
    A.x += (A.speed_x + AtoB_x * (G * B.math) / (2 * (distance ** 2))) * tick
    A.y += (A.speed_y + AtoB_y * (G * B.math) / (2 * (distance ** 2))) * tick
    B.x += (B.speed_x + BtoA_x * (G * A.math) / (2 * (distance ** 2))) * tick
    B.y += (B.speed_y + BtoA_y * (G * A.math) / (2 * (distance ** 2))) * tick


k = 0
while k < roop :
    history.append([[A.x,A.y],[B.x,B.y]])
    plt.plot((A.x,B.x),(A.y,B.y),".")
    move()
    print(k)
    k += 1

plt.savefig("output.png")
plt.show()

print(A.x,A.y)
print(B.x,B.y)
print(history)
print(distance)