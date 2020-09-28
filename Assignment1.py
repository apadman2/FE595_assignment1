# Importing libraries
import numpy as np
import matplotlib.pyplot as mp

# Creating data structure for Sine
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# Plotting Sine graph
mp.plot(x, y, linewidth=3, color='r')
mp.xlabel('x', fontweight=12)
mp.ylabel(r'$\sin(x)$', fontweight=12)
mp.title('Sine Function', fontweight=12)
mp.axhline(y=0, color='black', linestyle='-')
mp.show()

# Creating data structure for Sine
X = np.linspace(0, 2*np.pi, 100)
Y = np.cos(X)

# Plotting Cosine graph
mp.plot(X, Y, linewidth=3, color='r')
mp.xlabel('x', fontweight=12)
mp.ylabel(r'$\cos(x)$', fontweight=12)
mp.title('Cosine Function', fontweight=12)
mp.axhline(y=0, color='black', linestyle='-')
mp.show()
