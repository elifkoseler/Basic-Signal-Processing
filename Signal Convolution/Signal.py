import struct
import numpy as np
import wave
import scipy as sp
from scipy.io import wavfile
from scipy.io.wavfile import write

sound = wave.open("h3.wav","rb")
str1 = sound.readframes(1)
a1 = struct.unpack('hh',str1)
print("H3 ARRAY:")
print("a1: ", a1)
str2 = sound.readframes(1)
a2 = struct.unpack('hh',str2)
print("a2: ", a2)
str3 = sound.readframes(1)
a3 = struct.unpack('hh',str3)
print("a3: ", a3)

ason3 = a1+a2+a3
print(ason3)

sound = wave.open("h2.wav","rb")
str1 = sound.readframes(1)
a1 = struct.unpack('hh',str1)
print("H2 ARRAY:")
print("a1: ", a1)
str2 = sound.readframes(1)
a2 = struct.unpack('hh',str2)
print("a2: ", a2)
str3 = sound.readframes(1)
a3 = struct.unpack('hh',str3)
print("a3: ", a3)

ason2 = a1+a2+a3
print(ason2)

sound = wave.open("h1.wav","rb")
str1 = sound.readframes(1)
a1 = struct.unpack('hh',str1)
print("H1 ARRAY:")
print("a1: ", a1)
str2 = sound.readframes(1)
a2 = struct.unpack('hh',str2)
print("a2: ", a2)
str3 = sound.readframes(1)
a3 = struct.unpack('hh',str3)
print("a3: ", a3)


ason1 = a1+a2+a3
print(ason1)

aend = ason1+ason2+ason3
print("h[n]: ",aend)

sound = wave.open("input.wav","rb")
str1 = sound.readframes(1)
a1 = struct.unpack('hh',str1)
print("INPUT x[n]:")
print("a1: ", a1)
str2 = sound.readframes(1)
a2 = struct.unpack('hh',str2)
print("a2: ", a2)
str3 = sound.readframes(1)
a3 = struct.unpack('hh',str3)
print("a3: ", a3)

ain = a1+a2+a3
print(ain)

print(np.convolve(ain,aend))
rate=44000

write("y1.wav",rate,ason1)

write("y2.wav",rate,ason2)

wwrite("y3.wav",rate,ason3)
