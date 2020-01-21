import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(0, 2.0*np.pi, 101) 
y = np.sin(x) 
z = np.sinh(x)

xnumbers = np.linspace(10,15,20)
ynumbers1 = np.linspace(11,25,36)
ynumbers2 = np.linspace(33,88,44)

fig, ax1 = plt.subplots()                       # empty plot

ax2 = ax1.twinx()                               #axis ax1, ax2 will have same x axis limkts

curve1, = ax1.plot(x, y, label="sin", color='y') 
curve2, = ax2.plot(x, z, label="sinh", color='y')

curves = [curve1, curve2]
ax1.legend(curves, [curve.get_label() for curve in curves])

plt.title("Plot of sine and hyperbolic sine", color='y') 
plt.show()


