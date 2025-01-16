from create_moveBody import create_Body, move
from plotTraj import movets
import matplotlib.pyplot as plt

x,y= create_Body(24)
plt.plot(x,y,'.')
plt.show()
movets(0.1, 1, 50, x, y)
