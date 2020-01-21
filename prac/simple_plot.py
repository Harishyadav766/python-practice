import numpy as np 
import matplotlib.pyplot as plt
# angle varying between 0 and 2*pi 
x = np.linspace(0, 2.0*np.pi, 101)
y = np.sin(x)

xnumbers = np.linspace(0,7,15)
ynumbers = np.linspace(-1, 1, 11)
plt.plot(x, y, color='r', label='sin')
plt.xlabel("Angle in Radians") 
plt.ylabel("Magnitude") 
plt.title("Plot of some trigonometric functions")
plt.xticks(xnumbers)
plt.yticks(ynumbers)
plt.grid()
plt.legend()
plt.show()