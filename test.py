import numpy as np
import matplotlib.pyplot as plt

startr = 0.5
finalr = 4
max_time = 200
x = [0.1]
r = np.linspace(.5,4,200)

for n in range(0,200):

    x = np.append(r * x[n] * (1-x[n]))


plt.plot(x, label='x');
plt.xlabel('t');