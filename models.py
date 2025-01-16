import numpy as np


class Trajectory:
    x_tr_points = []
    y_tr_points = []
    
    def __init__(self, x_tr_points, y_tr_points):
        self.x_tr_points = x_tr_points
        self.y_tr_points = y_tr_points

    def __init__(self):
        self.x_tr_points = []
        self.y_tr_points = []

    def add(self, x, y):
        self.x_tr_points.append(x)
        self.y_tr_points.append(y)


class Streamline:
    def __init__(self, time, x1, x2):
        self.v1 = np.cosh(time) * x1
        self.v2 = np.sinh(time) * x2
