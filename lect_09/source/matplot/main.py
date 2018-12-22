import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
fig.suptitle('graphs')

x = np.linspace(0, 10, 500)

plt.plot(x, x, label='lin')
plt.plot(x, x**2, label='quad')
#plt.plot(x, x**3, label='cub')
plt.plot(x, 60*np.sin(x), label='sin')

plt.xlabel('x')
plt.ylabel('y')

plt.title("math graphs")

plt.legend()

plt.show()
