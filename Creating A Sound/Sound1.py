import numpy as np
import scipy.io.wavfile as wavfile

n = 1
x = np.arange(n)

y = np.sin(np.pi*x)+np.cos(np.pi*x)

y = np.tile(y,1000)

wavfile.write("sound1.wav",5000,y)
