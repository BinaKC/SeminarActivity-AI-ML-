import matplotlib.pyplot as plt
import numpy as np
x = np.array([[640, 970, 1120, 1580, 1900, 2130, 2460, 2610, 2880, 3200]]).T
y = np.array([[120, 123, 182, 167, 240, 284, 251, 272, 335, 340]]).T
plt.scatter(x, y)
plt.xlabel('Size (Sq Ft)')
plt.ylabel('Price, £ (x 1000)')
plt.show()