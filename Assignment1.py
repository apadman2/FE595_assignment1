# Importing libraries
import numpy as np
import matplotlib.pyplot as mp

# Creating data structure for Sine
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
z = np.cos(x)
t = np.tan(x)
mp.plot(x, y, x, z)
mp.plot(x,t)
mp.ylim(-3,3)
mp.xlabel('x')
mp.ylabel('Function value')
mp.title('Sine and Cosine functions')
mp.grid()
mp.show()

##### Review by Simran : code looks good!I suggest you can also add a legend here. Review 5/5

