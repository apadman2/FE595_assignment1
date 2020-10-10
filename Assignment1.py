# Importing libraries
import numpy as np
import matplotlib.pyplot as mp

# Creating data structure for Sine
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
z = np.cos(x)

mp.plot(x, y, x, z)
mp.xlabel('x')
mp.ylabel('Function value')
mp.title('Sine and Cosine functions')
mp.grid()
mp.show()



