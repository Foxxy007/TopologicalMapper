import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

config={"width":152, "length":42}

class Plotter:
    def __init__(self, config, values):
        pass
    def z_func(x, y):
        return x**2

ax = plt.axes(projection='3d')

x = np.linspace(0, config["width"], config["width"])
y = np.linspace(0, config["length"], config["length"])
print(x)
print(y)
X, Y = np.meshgrid(x, y)
print(list(X))
Z = Plotter.z_func(X, Y)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='coolwarm', edgecolor='none')
ax.set_title('Surface')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()