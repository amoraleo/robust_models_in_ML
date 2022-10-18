import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return x ** 2 - y ** 2

x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)

gradX = 2 * X
gradY = -2 * Y
dirX = gradX / np.sqrt(gradX**2 + gradY**2)
dirY = gradY/ np.sqrt(gradX**2 + gradY**2)

plt.quiver(X, Y, dirX, dirY, color='purple')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Поле направлений f(x,y)=x^2-y^2')
plt.show()