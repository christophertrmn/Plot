import math
import itertools
import matplotlib.pyplot as plt

try:
    namalegend = []
    mulai = int(input("How many trajectories?"))
    for x in range(mulai):
        namalegend.append("Ball {}".format(x + 1))
        initialvelocity = input("Enter the initial velocity for trajectory {} (m/s) ".format(x + 1))
        angle = input("Enter the angle of projection for trajectory {} (degrees) ".format(x + 1))

        speed_x = float(initialvelocity) * math.cos(math.radians(float(angle)))
        speed_y = float(initialvelocity) * math.sin(math.radians(float(angle)))

        xcor = list()
        ycor = list()

        for z in itertools.count():
            speedx = speed_x * (z / 1000)
            speedy = speed_y * (z / 1000) - 0.5 * 10 * (z / 1000) ** 2
            if speedy >= 0:
                xcor.append(speedx)
                ycor.append(speedy)
            else:
                break

        plt.scatter(xcor, ycor, s =10)

    plt.title("Projectile of the ball")
    plt.xlabel("X-Coordinate")
    plt.ylabel("Y-Coordinate")
    plt.legend(namalegend)
    plt.show()
except:
    print("ERROR PLEASE INPUT VALID INPUT")
