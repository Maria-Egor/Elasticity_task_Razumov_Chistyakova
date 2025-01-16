import math
import matplotlib.pyplot as plt
import models

def create_ring(n):
    coord_x = []  # массив из координат точек
    coord_y = []  # массив из координат точек
    x_c = 3  # положение центра кольца
    y_c = 3
    for r in range(2):
        for i in range(n):
            alpha = 2 * math.pi * i / n #угол
            x1 = x_c + (r + 1) * math.cos(alpha)
            y1 = y_c + (r + 1) * math.sin(alpha)

            coord_x.append(x1)
            coord_y.append(y1)
    return coord_x, coord_y


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


def move(t0, t, n, x0, y0):
    h = t / n
    tr = models.Trajectory()
    prx = x0
    pry = y0
    for i in range(n):
        x, y = runge_kutta(t0 + h * i, h, prx, pry)
        tr.add(x, y)
        prx = x
        pry = y
    return tr


def plottr(x,y):
    plt.plot(x,y)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('Траектория')
    plt.grid()

def plot_streamlines(time, min_val, max_val, skip=20):
    x_vals = np.linspace(1,min_val, abs(min_val) * 10 + 1)
    y_vals = np.linspace(1, max_val, max_val * 10 + 1)
    x, y = np.meshgrid(x_vals, y_vals)

    s = Streamline(time, x, y)

    x_decimated = x[::skip, ::skip]
    y_decimated = y[::skip, ::skip]
    v1_decimated = s.v1[::skip, ::skip]
    v2_decimated = s.v2[::skip, ::skip]

    plt.figure(figsize=(10, 6))
    plt.streamplot(x, y, s.v1, s.v2, density=1, color='red')
    plt.quiver(x_decimated, y_decimated, v1_decimated, v2_decimated, scale=100)
    plt.title(f'time = {round(time,1)}')
    plt.xlim(0, min_val)
    plt.ylim(0, max_val)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.show()

def movets(t0, t, n, x, y):
    for i in range(len(x)):
        res=move(t0, t, n, x[i], y[i])
        plottr(res.x_tr_points, res.y_tr_points)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.show()
