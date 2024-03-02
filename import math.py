import math
import matplotlib.pyplot as plt
from PIL import Image

tick = 60
roop = 100
pictures = []
G = 6.67430 * (10 ** -11)
Stars = []

class star() :
    """math:kg distance:m"""
    def __init__(self,x,y,math,speed_x,speed_y) :
        self.x = x
        self.y = y
        self.math = math
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self,Stars) :
        """StoK : Self to K"""
        for k in Stars :
            if k == self :
                continue
            distance = math.sqrt((k.x-self.x)**2 + (k.y-self.y)**2)
            StoK_x = k.x - self.x
            StoK_y = k.y - self.y
            self.speed_x += (StoK_x * G * (k.math) / (2 * (distance ** 2))) * tick
            self.speed_y += (StoK_y * G * (k.math) / (2 * (distance ** 2))) * tick
            self.x += self.speed_x
            self.y += self.speed_y

A = star(0,0,1.989 * (10 ** 30),0,0) # Sun
B = star(149597870700,0,5.972 * (10 ** 24),0,30556000) # Earth

distance = math.sqrt((A.x-B.x)**2 + (A.y-B.y)**2)

def move() :
    for i in Stars :
        i.move(Stars)

k = 0
while k < roop :
    plt.plot(A.x,A.y,".",c="red")
    plt.plot(B.x,B.y,".",c="green")
    plt.xlim(-200000000000,200000000000)
    plt.ylim(-200000000000,200000000000)
    plt.savefig(f"./images/{k}.png")
    pic_name = f"{k}.png"
    img = Image.open(f"./images/{pic_name}")
    pictures.append(img)
    move()
    print(k)
    k += 1

pictures[0].save('output.gif',save_all=True, append_images=pictures[1:],
optimize=True, duration=1, loop=0)

print("finished!")