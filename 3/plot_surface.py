import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return x ** 2 - y ** 2

x = np.linspace(-10, 10, 50)
y = np.linspace(-10, 10, 50)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot_surface(X, Y, Z)
ax.set_title('z=f(x,y)=x^2-y^2')
plt.show()