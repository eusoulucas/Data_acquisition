import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time
x = []
y = []
j = 0

plt.ion()
for i in range(0, 100):
    x.append(j)
    y.append(np.sin(j))
    plt.cla()
    plt.clf()
    plt.scatter(x, y)
    plt.savefig("figuras/graph" + str(i) + ".png")
    plt.pause(0.1)
    j += 0.1

plt.ioff()