import math
import matplotlib.pyplot as plt
from PIL import Image

tick = 60*60*24*365*100
roop = 1000
history = []
pictures = []

class star() :
    """math:kg distance:m"""
    def __init__(self,x,y,math,speed_x,speed_y) :
        self.x = x
        self.y = y
        self.math = math
        self.speed_x = speed_x
        self.speed_y = speed_y

A = star(-10000000,0,1 * 10^24,0,1)
B = star(10000000,0,10 * 10^24,0,-1)

distance = math.sqrt((A.x-B.x)**2 + (A.y-B.y)**2)

def move() :
    AtoB_x = B.x - A.x
    AtoB_y = B.y - A.y
    BtoA_x = A.x - B.x
    BtoA_y = A.y - B.y
    A.speed_x += AtoB_x * (B.math) / (2 * (distance ** 2)) * tick
    A.speed_y += AtoB_y * (B.math) / (2 * (distance ** 2)) * tick
    B.speed_x += BtoA_x * (A.math) / (2 * (distance ** 2)) * tick
    B.speed_y += BtoA_y * (A.math) / (2 * (distance ** 2)) * tick
    A.x += A.speed_x
    A.y += A.speed_y
    B.x += B.speed_x
    B.y += B.speed_y


k = 0
while k < roop :
    history.append([[A.x,A.y],[B.x,B.y]])
    plt.plot((A.x,B.x),(A.y,B.y),".",c="black")
    plt.savefig(f"./images/{k}.png")
    plt.cla
    pic_name = f"{k}.png"
    img = Image.open(f"./images/{pic_name}")
    pictures.append(img)
    move()
    print(k)
    k += 1

plt.show()

print(A.x,A.y)
print(B.x,B.y)
print(history)
print(distance)

pictures[0].save('output.gif',save_all=True, append_images=pictures[1:],
optimize=True, duration=1, loop=0)