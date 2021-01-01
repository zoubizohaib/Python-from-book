import numpy as np
import matplotlib.pyplot as plt

Many =50000

x = np.random.rand(Many)
#x = np.linspace(0.1,1.0, num= Many)
r = np.linspace(3.6,4.0, num= Many)



extra = np.array([])
for i in range(1, 3):
    x_a = 1-x
    Multi = np.multiply(x,r)
    Multi = np.multiply(Multi, x_a)
    x = Multi

    plt.title(r'Logistic map: $x_{n+1} = r x_{n} (1-x_{n}).$  n = '+ str(i) )
    plt.ylabel('x')
    plt.xlabel('r')
    #plt.plot(r, Multi,'o', mfc = 'k', ms = 0.1, mec='k')
    plt.scatter(r, Multi, s=0.1, c='k')
    #plt.show()
    plt.savefig(str(i) + "c. Graph.png", dpi = 300)
    plt.clf()
