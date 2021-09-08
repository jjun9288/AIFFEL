import numpy as np
import matplotlib.pyplot as plt
MU = 0
SIGMA = 1

def normal_dist(x):
    return (1/(np.sqrt(SIGMA*2*np.pi)))*(np.exp(-((x-MU)**2)/(2*SIGMA)))

x = np.linspace(-10,10,1000)
y = normal_dist(x)

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
