import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

t = sp.arange(-1*np.pi,1*np.pi,0.1)
x = np.cos(2*t*np.pi)*np.cos(2*t*np.pi)

plt.plot(t,x)
plt.show()
