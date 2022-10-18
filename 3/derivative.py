import math
import scipy
import matplotlib.pyplot as plt
import numpy as np

def func(x):
    return math.sin(x)
x_list = list(np.linspace(-5, 5, 1000))
y_list = [func(x) for x in x_list]
d_list = [scipy.misc.derivative(func, x, dx=1e-6) for x in x_list]

plt.plot(x_list, y_list, "b.", label="y = f(x)")
plt.plot(x_list, d_list, "r.", label="y = f'(x)")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графики функции f(x) и её производной')
plt.grid(visible=True, which="both", axis="both", linestyle="-")
plt.legend()
plt.show()