import math

def runge_kutta(t0, dt, x0, y0):
    kx1 = -math.cosh(t0) * x0
    kx2 = -math.cosh(t0 + 1 / 2 * dt) * (x0 + 1 / 2 * dt * kx1)
    kx3 = -math.cosh(t0 + 1 / 2 * dt) * (x0 + 1 / 2 * dt * kx2)
    kx4 = -math.cosh(t0 + dt) * (x0 + dt * kx3)
    x1 = x0 + dt * (kx1 + 2 * kx2 + 2 * kx3 + kx4) / 6

    ky1 = math.sinh(t0) * y0
    ky2 = math.sinh(t0 + 1 / 2 * dt) * (y0 + 1 / 2 * dt * ky1)
    ky3 = math.sinh(t0 + 1 / 2 * dt) * (y0 + 1 / 2 * dt * ky2)
    ky4 = math.sinh(t0 + dt) * (y0 + dt * ky3)
    y1 = y0 + dt * (ky1 + 2 * ky2 + 2 * ky3 + ky4) / 6

    return x1, y1


# проверка работы метода Рунге-Кутты
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.zeros(11)
y = np.zeros(11)
x[0] = 2
y[0] = 2
for i in range(0, 10):
    x[i + 1], y[i + 1] = runge_kutta(1 / 10 * i, 1 / 10, x[i], y[i])
t = np.linspace(0, 1, i + 2)

plt.plot(t, x)
plt.show()
"""
