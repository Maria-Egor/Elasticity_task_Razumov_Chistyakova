import methods
import matplotlib.pyplot as plt

x,y = methods.create_ring(24)
plt.plot(x,y,'.')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.show()
methods.movets(0.1, 1, 50, x, y)
