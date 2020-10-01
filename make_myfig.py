import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 1)
y = x**2

plt.figure()
plt.plot(x, y)

plt.xlabel('hours')
plt.ylabel('widgets')

plt.savefig('myfig.png')

