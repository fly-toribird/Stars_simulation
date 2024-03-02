import math
import matplotlib.pyplot as plt
from PIL import Image

tick = 60*60*24*365
roop = 1000
history = []
pictures = []
G = 6.67430 * (10 ** -11)

class star() :
    """math:kg distance:m"""
    def __init__(self,x,y,math,speed_x,speed_y) :
        self.x = x
        self.y = y
        self.math = math
        self.speed_x = speed_x
        self.speed_y = speed_y

A = star(0,0,1 * 10^24,0,100000) # Sun
B = star(149597870700,0,5.972 * (10 ** 24),30.556,0) # Earth
C = star(0,0,0,0,0)

distanceA_B = math.sqrt((A.x-B.x)**2 + (A.y-B.y)**2)
distanceB_C = math.sqrt((B.x-C.x)**2 + (B.y-C.y)**2)
distanceC_A = math.sqrt((C.x-A.x)**2 + (C.y-A.y)**2)

def move() :
    AtoB_x = B.x - A.x
    AtoB_y = B.y - A.y
    AtoC_x = C.x - A.x
    AtoC_y = C.y - A.y
    BtoA_x = A.x - B.x
    BtoA_y = A.y - B.y
    BtoC_x = C.x - B.x
    BtoC_y = C.y - B.y
    CtoA_x = A.x - C.x
    CtoA_y = A.y - C.y
    CtoB_x = B.x - C.x
    CtoB_y = B.y - C.y
    A.speed_x += (AtoB_x * G * (B.math) / (2 * (distanceA_B ** 2)) + AtoC_x * G * (C.math) / (2 * (distanceC_A ** 2))) * tick
    A.speed_y += (AtoB_y * G * (B.math) / (2 * (distanceA_B ** 2)) + AtoC_y * G * (C.math) / (2 * (distanceC_A ** 2))) * tick
    B.speed_x += (BtoA_x * G * (A.math) / (2 * (distanceA_B ** 2)) + BtoC_x * G * (C.math) / (2 * (distanceB_C ** 2))) * tick
    B.speed_y += (BtoA_y * G * (A.math) / (2 * (distanceA_B ** 2)) + BtoC_y * G * (C.math) / (2 * (distanceB_C ** 2))) * tick
    C.speed_x += (CtoB_x * G * (B.math) / (2 * (distanceB_C ** 2)) + CtoA_x * G * (A.math) / (2 * (distanceC_A ** 2))) * tick
    C.speed_y += (CtoB_y * G * (B.math) / (2 * (distanceB_C ** 2)) + CtoA_y * G * (A.math) / (2 * (distanceC_A ** 2))) * tick
    A.x += A.speed_x
    A.y += A.speed_y
    B.x += B.speed_x
    B.y += B.speed_y
    C.x += C.speed_x
    C.y += C.speed_y


k = 0
while k < roop :
    history.append([[A.x,A.y],[B.x,B.y],[C.x,C.y]])
    plt.plot(A.x,A.y,".",c="red")
    plt.plot(B.x,B.y,".",c="green")
    plt.plot(C.x,C.y,".",c="blue")
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