import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

t = np.linspace(-4, 4, 100)

plt.subplot(2,1,1)
plt.plot(t, np.exp(1j*np.pi*t).real )
plt.xlabel('t')
plt.ylabel('Re x(t)')
plt.title(r'Real part of  $x(t)=e^{j \pi t}$')
plt.xlim([-4, 4]);

plt.subplot(2,1,2);
plt.plot(t, np.exp(1j*np.pi*t).imag);
plt.xlabel('t');
plt.ylabel('Im x(t)');
plt.title(r'Imaginary part of  $x(t)=e^{j \pi t}$');

plt.xlim([-4, 4]);
plt.show()