import numpy as np
import matplotlib.pyplot as plt
r = float(input("Pleae enter a value of r: "))
x = float(input("Pleae enter a value of x [0-1]: "))
Itrations  = int(input("How many iterations : "))

Range = 0
Data = []
while Range != Itrations:

    x = r*x*(1-x)
   
    Data.append(x)
    y = np.array(Data)

    plt.plot(y, 'o-', ms = 5)
    plt.savefig(str(Range) + " Graph.png", dpi = 300)
    Range += 1

