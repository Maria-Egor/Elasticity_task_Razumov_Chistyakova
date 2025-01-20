import methods
import matplotlib.pyplot as plt
import numpy as np

x,y = methods.create_ring(24)
plt.plot(x,y,'.')
plt.grid(color='gray', linestyle='--', linewidth=0.5)

plt.axis('equal')
plt.show()
[x_end,y_end]=methods.movets(0, 1, 50, x, y)
methods.deformation(x, y, x_end, y_end)

for t in np.arange(0.1, 1.1, 0.1):
    methods.plot_streamlines(t, 10, 10)
